import argparse


def calculate_pv_of_cash_flow(
    nom_price: float,
    cou_rate: float,
    dis_rate: float,
    duration: float,
    period: float = 1,
) -> float:
    """
    Calculate the present cash flow by using coupon rate and discount rate.

    Args:
        nom_price (float): Nominal Value.
        cou_rate (float): Lender provided this rate to bond owner (in percentage per annum).
        dis_rate (float): The discount rate used to calculate the present value of future cash flows (in percentage per annum).
        duration (float): Duration in years (for six months use 0.5).
        period (float, optional): Number of periods in a year. Defaults to 1.

    Returns:
        float: The present value of the bond.
    """

    no_of_periods = period * duration
    if int(no_of_periods) != no_of_periods:
        raise ValueError("Multiplication of periods and duration should be an integer.")

    updated_cou_rate = cou_rate / (period * 100)
    updated_dis_rate = dis_rate / (period * 100)

    pv_of_all_int_pay = 0
    for period in range(1, int(no_of_periods) + 1):
        # Calculate present value of interest received per period
        pv_of_int_pay = nom_price * updated_cou_rate / ((1 + updated_dis_rate) ** period)
        pv_of_all_int_pay += pv_of_int_pay

    # Adding the present value of the nominal value
    present_value_of_nom_price = nom_price / ((1 + updated_dis_rate) ** int(no_of_periods))
    pv_of_cash_flow = pv_of_all_int_pay + present_value_of_nom_price
    return round(pv_of_cash_flow, 2)


def main():
    parser = argparse.ArgumentParser(description="Calculate Present Value of Cash Flow")
    parser.add_argument("--nom_price", type=float, default=1000000.0)
    parser.add_argument("--cou_rate", type=float, default=4.5)
    parser.add_argument("--dis_rate", type=float, default=5.0)
    parser.add_argument("--duration", type=float, default=5)
    parser.add_argument("--period", type=float, default=1)

    args = parser.parse_args()

    result = calculate_pv_of_cash_flow(
        args.nom_price, args.cou_rate, args.dis_rate, args.duration, args.period
    )
    print(f"Present Value of Cash Flow is {result:,} for nominal value of {args.nom_price:,} after {args.duration} Years" )


if __name__ == "__main__":
    main()
