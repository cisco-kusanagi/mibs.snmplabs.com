#
# PySNMP MIB module CTRON-POWER-SUPPLY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-POWER-SUPPLY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:44:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ctps, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctps")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Integer32, Counter32, Counter64, NotificationType, ObjectIdentity, iso, MibIdentifier, ModuleIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Integer32", "Counter32", "Counter64", "NotificationType", "ObjectIdentity", "iso", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
chPower = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1))
boardPower = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2))
psPower = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3))
bbuPower = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 4))
termPower = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5))
chPowerOperationalStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("powerAC", 1), ("powerACRedundant", 2), ("powerDC", 3), ("powerDCRedundant", 4), ("battery", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerOperationalStatus.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerOperationalStatus.setDescription("This object reflects the overall status of the chassis's power supply in terms of how the power is being delivered to the chassis.")
chPowerMainVoltageStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("powerOK", 1), ("overCurrent", 2), ("overVoltage", 3), ("underVoltage", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerMainVoltageStatus.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerMainVoltageStatus.setDescription('This object reflects the state of the main voltage rail within the chassis. The power on this rail may be delivered by AC supplies, DC supplies or battery supplies.')
chPowerMainVoltage = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerMainVoltage.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerMainVoltage.setDescription("The voltage of the chassis's main voltage rail. This rail carries power to all the modules in the chassis. It has an allowable range of 40 volts to 60 volts DC. The value of this object is the actual voltage * 10.")
chPowerTotalSupply = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerTotalSupply.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerTotalSupply.setDescription("The total power being supplied by the chassis's power supplies to the chassis. The value of this object is the actual watts.")
chPowerTotalLoad = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerTotalLoad.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerTotalLoad.setDescription("The total load being presented by the chassis to the chassis's power supplies. The value of this object is the actual watts.")
chPowerMaxSupply = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerMaxSupply.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerMaxSupply.setDescription("The maximum power that could de supplied by the chassis's power supplies to the chassis. The value of this object is the actual watts.")
chPowerMaxLoad = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerMaxLoad.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerMaxLoad.setDescription("The maximum load that could be presented by the chassis to the chassis's power supplies. The value of this object is the actual watts.")
chPowerTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8), )
if mibBuilder.loadTexts: chPowerTable.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerTable.setDescription("A list of power lines or busses on the chassis's backplane.")
chPowerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1), ).setIndexNames((0, "CTRON-POWER-SUPPLY-MIB", "chPowerLineID"))
if mibBuilder.loadTexts: chPowerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerEntry.setDescription('A slot entry containing objects for a particular module and associated power line.')
chPowerLineID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerLineID.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerLineID.setDescription("A unique value used to identify a particular power line on the chassis's backplane.")
chPowerLineType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 2), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerLineType.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerLineType.setDescription('The type of power. For example, a power line that supplies DC current at a nominal voltage of 40 to 57 volts or a power line that supplies AC current at a nominal volatge of 110v.')
chPowerLineTotalSupply = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerLineTotalSupply.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerLineTotalSupply.setDescription("The total power being supplied by the chassis's power supplies to the chassis on this power line. The value of this object is the actual watts.")
chPowerLineTotalLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerLineTotalLoad.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerLineTotalLoad.setDescription("The total load being presented by the chassis to the chassis's power supplies on this power line. This value will be zero if unknown The value of this object is the actual watts.")
chPowerLineMaxSupply = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerLineMaxSupply.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerLineMaxSupply.setDescription("The maximum power that could de supplied by the chassis's power supplies to the chassison this power line. The value of this object is the actual watts.")
chPowerLineMaxLoad = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 8, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerLineMaxLoad.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerLineMaxLoad.setDescription("The maximum load that could be presented by the chassis to the chassis's power supplies on this power line. The value of this object is the actual watts.")
chPowerDiagVoltageStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("powerOK", 1), ("overCurrent", 2), ("overVoltage", 3), ("underVoltage", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerDiagVoltageStatus.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerDiagVoltageStatus.setDescription('This object reflects the state of the diag voltage rail within the chassis.')
chPowerDiagVoltage = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: chPowerDiagVoltage.setStatus('mandatory')
if mibBuilder.loadTexts: chPowerDiagVoltage.setDescription("The voltage of the chassis's diag voltage rail. This rail carries power to all the modules in the chassis. It has an allowable range of 4.75 volts to 5.25 volts DC. The value of this object is the actual voltage * 10.")
boardPowerSlotStatusTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1), )
if mibBuilder.loadTexts: boardPowerSlotStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerSlotStatusTable.setDescription('A list of networking modules installed in this chassis.')
boardPowerSlotStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1), ).setIndexNames((0, "CTRON-POWER-SUPPLY-MIB", "boardPowerSlotStatusID"))
if mibBuilder.loadTexts: boardPowerSlotStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerSlotStatusEntry.setDescription('A slot entry containing objects for a particular module.')
boardPowerSlotStatusID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerSlotStatusID.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerSlotStatusID.setDescription('The slot number of a chassis slot in which this board is installed. This object is similiar to chSlotID in the Chassis MIB.')
boardPowerOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))).clone(namedValues=NamedValues(("powerOn", 1), ("powerOff", 2), ("reset", 3), ("overVoltage", 4), ("underVoltage", 5), ("overCurrent", 6), ("overCurrentShutdown", 7), ("temperatureShutdown", 8), ("remotePowerOff", 9), ("powerConservationShutdown", 10), ("frontPanelPowerOff", 11)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerOperationalStatus.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerOperationalStatus.setDescription("This object reflects the status of the module's DC-DC converter power supply.")
boardPowerAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("powerOn", 1), ("powerOff", 2), ("reset", 3))).clone('powerOn')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boardPowerAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerAdminStatus.setDescription("This object controls the operation of the module's DC-DC power supply. If the value 3 is written to this object then the value of the object will be set to 1 after the reset is performed.")
boardPowerLocalAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("localMode", 1), ("secureMode", 2))).clone('localMode')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boardPowerLocalAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerLocalAdminStatus.setDescription("This object controls the operation of the module's front panel button. In local mode this button may be used to locally control the operation of the DC-DC converter, i.e. power on, power off and reset. In secure mode a request the state of the front panel button is reflected in the object boardPowerOperationalStatus. In secure mode the front panel button has no effect locally.")
boardPowerLocalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("resetRequest", 1), ("powerDownRequest", 2), ("powerOnRequest", 3), ("normal", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerLocalStatus.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerLocalStatus.setDescription("This object reflects the state of the module's front panel button.")
boardPowerShutdownAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enabled", 1), ("disabled", 2))).clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boardPowerShutdownAdmin.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerShutdownAdmin.setDescription('This object controls whether or not the module should auto power down due to an fault condition.')
boardPowerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 14)).clone(14)).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boardPowerPriority.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerPriority.setDescription("The module's power-up and power down priority. This is a value of 1 to 14 and is used to decide which modules are allowed to power on in the event that power demand of the chassis is greater than the total power supply. The default value is 14, highest priority. When two modules have equal priority then the module in the lowest slot wins.")
boardPowerMaxInputPower = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerMaxInputPower.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerMaxInputPower.setDescription('The maximum input power that this module is allowed to consume. The value of this object is actual watts.')
boardPowerManagement = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 7))).clone(namedValues=NamedValues(("disabled", 1), ("enabled", 2), ("not-supported", 7))).clone('not-supported')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: boardPowerManagement.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerManagement.setDescription('Module power management status.')
boardPowerSlotTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2), )
if mibBuilder.loadTexts: boardPowerSlotTable.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerSlotTable.setDescription('A list of networking modules and associated power lines installed in this chassis.')
boardPowerSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1), ).setIndexNames((0, "CTRON-POWER-SUPPLY-MIB", "boardPowerSlotID"), (0, "CTRON-POWER-SUPPLY-MIB", "boardPowerID"))
if mibBuilder.loadTexts: boardPowerSlotEntry.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerSlotEntry.setDescription('A slot entry containing objects for a particular module and associated power line.')
boardPowerSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerSlotID.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerSlotID.setDescription('The slot number of a chassis slot in which this board is installed. This object is similiar to chSlotID in the Chassis MIB.')
boardPowerID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerID.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerID.setDescription('A unique value used to identify a particular power line.')
boardPowerType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerType.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerType.setDescription('The type of power. For example, a power line that supplies DC current at a nominal voltage of 40 to 57 volts or a power line that supplies AC current at a nominal volatge of 110v.')
boardPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("powerOK", 1), ("powerOff", 2), ("overCurrent", 3), ("overVoltage", 4), ("underVoltage", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerStatus.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerStatus.setDescription('This object reflects the status of this power line.')
boardPowerVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 5), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerVoltage.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerVoltage.setDescription('The voltage reading for the power line. The value of this object is actual voltage * 100.')
boardPowerCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerCurrent.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerCurrent.setDescription('The current reading for the power line. The value of this object is the actual amperage * 100. If this reading is not implemented then value will be zero.')
boardPowerMaxVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerMaxVoltage.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerMaxVoltage.setDescription('The maximum voltage for this power line. If the voltage reading for this power line is greater than this value then the power line is considered to be in an overvolatge condition. The value of this object is in voltage * 100.')
boardPowerMinVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerMinVoltage.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerMinVoltage.setDescription('The minimum voltage for this power line. If the voltage reading for this power line is less than this value then the power line is considered to be in an undervolatge condition. The value of this object is voltage * 100.')
boardPowerMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 2, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: boardPowerMaxPower.setStatus('mandatory')
if mibBuilder.loadTexts: boardPowerMaxPower.setDescription('The maximum power for this power line. If the power calculated for this power line is greater than this value then the power line is considered to be in an overload condition. The value of this object is in watts.')
psPowerSlotStatusTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1), )
if mibBuilder.loadTexts: psPowerSlotStatusTable.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerSlotStatusTable.setDescription('A list of AC & DC power supplies installed in this chassis.')
psPowerSlotStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1), ).setIndexNames((0, "CTRON-POWER-SUPPLY-MIB", "psPowerSlotStatusID"))
if mibBuilder.loadTexts: psPowerSlotStatusEntry.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerSlotStatusEntry.setDescription('A slot entry containing objects for a particular power supply.')
psPowerSlotStatusID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerSlotStatusID.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerSlotStatusID.setDescription('The slot number of a chassis slot in which this AC power supply is installed. This object is similiar to chSlotID in the Chassis MIB.')
psPowerOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))).clone(namedValues=NamedValues(("powerOn", 1), ("powerOff", 2), ("reset", 3), ("overVoltage", 4), ("underVoltage", 5), ("overCurrent", 6), ("overCurrentShutdown", 7), ("temperatureShutdown", 8), ("remotePowerOff", 9)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerOperationalStatus.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerOperationalStatus.setDescription("This object reflects the status of the module's DC-DC converter power supply.")
psPowerAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("powerOn", 1), ("powerOff", 2))).clone('powerOn')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psPowerAdminStatus.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerAdminStatus.setDescription('This object controls the operation of power supply.')
psPowerMaxOutputPower = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 1, 1, 4), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerMaxOutputPower.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerMaxOutputPower.setDescription('The maximum power that this power supply is allowed to ouput. The value of this object is watts.')
psPowerSlotTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2), )
if mibBuilder.loadTexts: psPowerSlotTable.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerSlotTable.setDescription('A list of power supplies and associated power lines installed in this chassis.')
psPowerSlotEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1), ).setIndexNames((0, "CTRON-POWER-SUPPLY-MIB", "psPowerSlotID"), (0, "CTRON-POWER-SUPPLY-MIB", "psPowerID"))
if mibBuilder.loadTexts: psPowerSlotEntry.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerSlotEntry.setDescription('A slot entry containing objects for a particular power line on a particular power supply.')
psPowerSlotID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 1), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerSlotID.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerSlotID.setDescription('The slot number of a chassis slot in which this Power supply is installed. This object is similiar to chSlotID in the Chassis MIB.')
psPowerID = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerID.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerID.setDescription('A unique value used to identify a particular power line.')
psPowerType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 3), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerType.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerType.setDescription('The type of power. For example, a power line that supplies DC current at a nominal voltage of 40 to 57 volts or a power line that supplies AC current at a nominal volatge of 110v.')
psPowerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("powerOK", 1), ("powerOff", 2), ("overCurrent", 3), ("overVoltage", 4), ("underVoltage", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerStatus.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerStatus.setDescription('This object reflects the status of the power line.')
psPowerAdmin = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("powerOn", 1), ("powerOff", 2))).clone('powerOn')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: psPowerAdmin.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerAdmin.setDescription('This object controls the operation of power supply.')
psPowerVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 6), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerVoltage.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerVoltage.setDescription('The voltage reading for the power line. The value of this object is the actual voltage * 100.')
psPowerCurrent = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 7), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerCurrent.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerCurrent.setDescription('The current reading for the power line. The value of this object is amperage * 100. If this reading is not implemented then value will be zero.')
psPowerLineFrequency = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 8), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerLineFrequency.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerLineFrequency.setDescription('The line frequency for the power line. The value of this object is the actual frequency in Hertz * 10. If this reading is not implemented then value will be zero.')
psPowerMaxVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerMaxVoltage.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerMaxVoltage.setDescription('The maximum voltage for this power line. If the voltage reading for this power line is greater than this value then the power line is considered to be in an over volatge condition. The value of this object is voltage * 100.')
psPowerMinVoltage = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 10), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerMinVoltage.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerMinVoltage.setDescription('The minimum voltage for this power line. If the voltage reading for this power line is greater than this value then the power line is considered to be in an over volatge condition. The value of this object is voltage * 100.')
psPowerMaxPower = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 3, 2, 1, 11), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: psPowerMaxPower.setStatus('mandatory')
if mibBuilder.loadTexts: psPowerMaxPower.setDescription('The maximum power for this power line. If the power calculated for this power line is greater than this value then the power line is considered to be in an overload condition. The value of this object is watts.')
termPowerStatus = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("powerOK", 1), ("overCurrent", 2), ("overVoltage", 3), ("underVolatge", 4), ("overPower", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: termPowerStatus.setStatus('mandatory')
if mibBuilder.loadTexts: termPowerStatus.setDescription("This object reflects the status of the chassis's termination voltage rail.")
termPowerVoltage = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 2), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: termPowerVoltage.setStatus('mandatory')
if mibBuilder.loadTexts: termPowerVoltage.setDescription("The voltage of the chassis's termination voltage rail. This rail carries power to INB terminator cards in the chassis. It has an allowalble range of 3.3 Volt + or - 5%.The value of this object is voltage * 100.")
termPowerCurrent = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 3), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: termPowerCurrent.setStatus('mandatory')
if mibBuilder.loadTexts: termPowerCurrent.setDescription("The current on the chassis's termination voltage rail. The value of this object is the actual amperage * 100. If this reading is not implemented then the value will be zero.")
termPowerModule1Status = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("normal", 1), ("iNBaFault", 2), ("iNBbFault", 3), ("fault", 4), ("termModuleNotInstalled", 5), ("unknown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: termPowerModule1Status.setStatus('mandatory')
if mibBuilder.loadTexts: termPowerModule1Status.setDescription('This object reflects the state of the INB termination module number 1. A value of normal(1) reflects that both busses are normal. A value of fault(4) reflects that both busses are in a fault condition.')
termPowerModule2Status = MibScalar((1, 3, 6, 1, 4, 1, 52, 4, 1, 1, 7, 5, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))).clone(namedValues=NamedValues(("normal", 1), ("iNBaFault", 2), ("iNBbFault", 3), ("fault", 4), ("termModuleNotInstalled", 5), ("unknown", 6)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: termPowerModule2Status.setStatus('mandatory')
if mibBuilder.loadTexts: termPowerModule2Status.setDescription('This object reflects the state of the INB termination module number 2. A value of normal(1) reflects that both busses are normal. A value of fault(4) reflects that both busses are in a fault condition.')
mibBuilder.exportSymbols("CTRON-POWER-SUPPLY-MIB", chPowerEntry=chPowerEntry, chPowerLineMaxLoad=chPowerLineMaxLoad, psPowerMaxVoltage=psPowerMaxVoltage, chPowerLineTotalLoad=chPowerLineTotalLoad, boardPowerSlotStatusEntry=boardPowerSlotStatusEntry, boardPowerSlotTable=boardPowerSlotTable, psPowerSlotID=psPowerSlotID, chPowerTotalLoad=chPowerTotalLoad, chPowerTable=chPowerTable, chPowerLineTotalSupply=chPowerLineTotalSupply, boardPowerShutdownAdmin=boardPowerShutdownAdmin, psPowerAdmin=psPowerAdmin, termPowerCurrent=termPowerCurrent, boardPowerSlotEntry=boardPowerSlotEntry, chPowerMainVoltage=chPowerMainVoltage, psPowerLineFrequency=psPowerLineFrequency, termPowerModule1Status=termPowerModule1Status, boardPowerType=boardPowerType, boardPowerPriority=boardPowerPriority, psPowerMaxOutputPower=psPowerMaxOutputPower, psPowerVoltage=psPowerVoltage, psPower=psPower, psPowerSlotStatusEntry=psPowerSlotStatusEntry, chPowerMaxLoad=chPowerMaxLoad, psPowerSlotStatusID=psPowerSlotStatusID, psPowerSlotTable=psPowerSlotTable, termPowerModule2Status=termPowerModule2Status, boardPowerManagement=boardPowerManagement, boardPowerLocalStatus=boardPowerLocalStatus, boardPowerMaxVoltage=boardPowerMaxVoltage, boardPowerLocalAdminStatus=boardPowerLocalAdminStatus, boardPowerAdminStatus=boardPowerAdminStatus, chPowerMainVoltageStatus=chPowerMainVoltageStatus, boardPowerID=boardPowerID, psPowerID=psPowerID, bbuPower=bbuPower, boardPowerOperationalStatus=boardPowerOperationalStatus, psPowerSlotStatusTable=psPowerSlotStatusTable, psPowerMinVoltage=psPowerMinVoltage, boardPowerSlotStatusID=boardPowerSlotStatusID, boardPowerSlotID=boardPowerSlotID, boardPowerMaxInputPower=boardPowerMaxInputPower, termPowerVoltage=termPowerVoltage, boardPowerStatus=boardPowerStatus, boardPowerMinVoltage=boardPowerMinVoltage, psPowerCurrent=psPowerCurrent, chPowerLineType=chPowerLineType, chPower=chPower, chPowerDiagVoltage=chPowerDiagVoltage, psPowerAdminStatus=psPowerAdminStatus, psPowerSlotEntry=psPowerSlotEntry, chPowerLineMaxSupply=chPowerLineMaxSupply, boardPowerCurrent=boardPowerCurrent, chPowerTotalSupply=chPowerTotalSupply, boardPowerMaxPower=boardPowerMaxPower, boardPowerVoltage=boardPowerVoltage, chPowerMaxSupply=chPowerMaxSupply, psPowerType=psPowerType, psPowerMaxPower=psPowerMaxPower, boardPowerSlotStatusTable=boardPowerSlotStatusTable, termPower=termPower, chPowerDiagVoltageStatus=chPowerDiagVoltageStatus, chPowerOperationalStatus=chPowerOperationalStatus, chPowerLineID=chPowerLineID, psPowerOperationalStatus=psPowerOperationalStatus, psPowerStatus=psPowerStatus, boardPower=boardPower, termPowerStatus=termPowerStatus)
