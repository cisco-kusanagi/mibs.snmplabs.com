#
# PySNMP MIB module AOLAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AOLAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:22:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, enterprises, Counter32, Unsigned32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, NotificationType, Bits, Gauge32, ModuleIdentity, IpAddress, NotificationType, ObjectIdentity, Counter64, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "enterprises", "Counter32", "Unsigned32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "NotificationType", "Bits", "Gauge32", "ModuleIdentity", "IpAddress", "NotificationType", "ObjectIdentity", "Counter64", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
intel = MibIdentifier((1, 3, 6, 1, 4, 1, 343))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2))
mangement_products = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 8)).setLabel("mangement-products")
tCO_products = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 8, 1)).setLabel("tCO-products")
alert_on_LAN = MibIdentifier((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1)).setLabel("alert-on-LAN")
systemName = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 1), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemName.setStatus('current')
if mibBuilder.loadTexts: systemName.setDescription('System NetBIOS name')
systemGUID = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: systemGUID.setStatus('current')
if mibBuilder.loadTexts: systemGUID.setDescription("System's GUID")
eventString = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventString.setStatus('current')
if mibBuilder.loadTexts: eventString.setDescription('Additional event information string.')
eventInfo = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(9, 9)).setFixedLength(9)).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventInfo.setStatus('current')
if mibBuilder.loadTexts: eventInfo.setDescription('Additional information associated with the event.')
iPAddress = MibScalar((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(16, 16)).setFixedLength(16)).setMaxAccess("readonly")
if mibBuilder.loadTexts: iPAddress.setStatus('current')
if mibBuilder.loadTexts: iPAddress.setDescription('IP Address of trap originator.')
presenceHeartbeat = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,0)).setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: presenceHeartbeat.setDescription('Presence Heartbeat Expired')
coverTamper = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,1)).setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: coverTamper.setDescription('Cover Tamper')
voltage_Fan_Temperature = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,2)).setLabel("voltage-Fan-Temperature").setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: voltage_Fan_Temperature.setDescription('Voltage/Fan/Temperature Out of Specification')
lANLeash = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,3)).setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: lANLeash.setDescription('LAN Leash Tamper')
temperature = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,4)).setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: temperature.setDescription('Temperature Out of Specification')
processorMissing = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,5)).setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: processorMissing.setDescription('Processor Missing')
processorTemperature = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,6)).setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: processorTemperature.setDescription('Processor Over Temperature')
watchdog = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,7)).setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: watchdog.setDescription('Watchdog Event')
p_O_S_T = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,8)).setLabel("p-O-S-T").setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: p_O_S_T.setDescription('P.O.S.T.')
unknownEvent = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,9)).setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: unknownEvent.setDescription('Unknown Event')
processor_0_Missing = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,10)).setLabel("processor-0-Missing").setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: processor_0_Missing.setDescription('Processor 0 Missing')
processor_1_Missing = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,11)).setLabel("processor-1-Missing").setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: processor_1_Missing.setDescription('Processor 1 Missing')
voltage_Fan = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,12)).setLabel("voltage-Fan").setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: voltage_Fan.setDescription('Voltage/Fan Out of Specification')
voltage = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,13)).setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: voltage.setDescription('Voltage Out of Specification')
fan = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,14)).setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: fan.setDescription('Fan Out of Specification')
fan_Temperature = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,15)).setLabel("fan-Temperature").setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: fan_Temperature.setDescription('Fan/Temperature Out of Specification')
voltage_Temperature = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,16)).setLabel("voltage-Temperature").setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: voltage_Temperature.setDescription('Voltage/Temperature Out of Specification')
undock = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,17)).setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: undock.setDescription('Surprised Undock event')
eventClear = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,18)).setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: eventClear.setDescription('Event clear')
clientAdded = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,19)).setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: clientAdded.setDescription('Client added')
clientDeleted = NotificationType((1, 3, 6, 1, 4, 1, 343, 2, 8, 1, 1) + (0,20)).setObjects(("AOLAN-MIB", "systemName"))
if mibBuilder.loadTexts: clientDeleted.setDescription('Client deleted')
mibBuilder.exportSymbols("AOLAN-MIB", alert_on_LAN=alert_on_LAN, systemGUID=systemGUID, intel=intel, voltage_Temperature=voltage_Temperature, coverTamper=coverTamper, processorMissing=processorMissing, undock=undock, mangement_products=mangement_products, temperature=temperature, watchdog=watchdog, eventString=eventString, systemName=systemName, eventInfo=eventInfo, voltage_Fan=voltage_Fan, presenceHeartbeat=presenceHeartbeat, lANLeash=lANLeash, fan=fan, clientAdded=clientAdded, voltage=voltage, clientDeleted=clientDeleted, unknownEvent=unknownEvent, processorTemperature=processorTemperature, tCO_products=tCO_products, processor_0_Missing=processor_0_Missing, eventClear=eventClear, voltage_Fan_Temperature=voltage_Fan_Temperature, processor_1_Missing=processor_1_Missing, fan_Temperature=fan_Temperature, iPAddress=iPAddress, p_O_S_T=p_O_S_T, products=products)
