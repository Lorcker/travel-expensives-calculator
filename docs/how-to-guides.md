This part of the project documentation focuses on a
**problem-oriented** approach.

## How to start the application

1. Download the application
2. Run config
3. Run program

## How to use the application

Given use case:
You went on vacation with your friends they spent money on behalf of the group the following way:

- _Christian_ spent _300€_ in total
- _Cevin_ spent _60€_ in total
- _Nils_ spent _70€_ in total
- _Robin_, _Jana_, _Nora_ spent _0€_

Now in order to figure out who has to transfer what amount of money to which person, in order to distribute expenses evenly among the group do the following:

1. Select **Add person** in the menu by using up/down key and press Enter

```
? Select an action:
❯ Add person
Calculate Transactions
Exit
```

2. Enter the **Name** of the person using your keyboard:

```
? Select an action: Add person
? Enter name of the person: Christian
```

3. Enter how much money _Christian_ has spent:

```
? Select an action: Add person
? Enter name of the person: Christian
? Enter spendings of Christian: 300 . 0
```

4. Repeat steps 1-3 until you entered every person
5. Select **Calculate Transactions** in the menu by using up/down key and press Enter

```
? Select an action:
  Add person
❯ Calculate Transactions
  Exit
```

6. You can happily watch the output of the application:

```
All these people had fun
        together:
┏━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ Name      ┃ Spendings ┃
┡━━━━━━━━━━━╇━━━━━━━━━━━┩
│ Christian │ 300.00€   │
│           │           │
│ Cevin     │ 60.00€    │
│           │           │
│ Nils      │ 70.00€    │
│           │           │
│ Robin     │ 0.00€     │
│           │           │
│ Jaba      │ 0.00€     │
│           │           │
│ Nora      │ 0.00€     │
└───────────┴───────────┘

╭─ Total spendings ─╮ ╭─ Debt per person ─╮
│ 430.00€           │ │ 71.67€            │
╰───────────────────╯ ╰───────────────────╯

Following Transactions have to be
            made:
┏━━━━━━━┳━━━━━┳━━━━━━━━━━━┳━━━━━━━━┓
┃ From  ┃     ┃ To        ┃ Amount ┃
┡━━━━━━━╇━━━━━╇━━━━━━━━━━━╇━━━━━━━━┩
│ Cevin │ --> │ Christian │ 11.67€ │
│       │     │           │        │
│ Nils  │ --> │ Christian │ 1.67€  │
│       │     │           │        │
│ Robin │ --> │ Christian │ 71.67€ │
│       │     │           │        │
│ Jaba  │ --> │ Christian │ 71.67€ │
│       │     │           │        │
│ Nora  │ --> │ Christian │ 71.67€ │
└───────┴─────┴───────────┴────────┘
```
