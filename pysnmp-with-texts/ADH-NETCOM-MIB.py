#
# PySNMP MIB module ADH-NETCOM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ADH-NETCOM-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:13:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, NotificationType, Integer32, Unsigned32, IpAddress, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, iso, ModuleIdentity, Bits, Counter64, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "NotificationType", "Integer32", "Unsigned32", "IpAddress", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "iso", "ModuleIdentity", "Bits", "Counter64", "Counter32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
environmentalTechnology = ModuleIdentity((1, 3, 6, 1, 4, 1, 32185))
environmentalTechnology.setRevisions(('2010-02-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: environmentalTechnology.setRevisionsDescriptions(('ADH NETCOM: Ethernet-enabled air dehydrator.',))
if mibBuilder.loadTexts: environmentalTechnology.setLastUpdated('201002100000Z')
if mibBuilder.loadTexts: environmentalTechnology.setOrganization('Environmental Technology Inc.')
if mibBuilder.loadTexts: environmentalTechnology.setContactInfo(' Environmental Technology Inc. Product Support Postal: 1850 N. Sheridan St. South Bend, IN 46628 USA Tel: +1 574 233 1202 E-mail: cgartland@networketi.com')
if mibBuilder.loadTexts: environmentalTechnology.setDescription('The Structure of Management Information for Environmental Technology Inc. SNMP devices')
netcom = ObjectIdentity((1, 3, 6, 1, 4, 1, 32185, 2))
if mibBuilder.loadTexts: netcom.setStatus('current')
if mibBuilder.loadTexts: netcom.setDescription(' ADH NETCOM')
statusInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 32185, 2, 1))
paramsInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 32185, 2, 2))
allStatuses = MibScalar((1, 3, 6, 1, 4, 1, 32185, 2, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(80, 80)).setFixedLength(80)).setMaxAccess("readonly")
if mibBuilder.loadTexts: allStatuses.setStatus('current')
if mibBuilder.loadTexts: allStatuses.setDescription('Summary: same as objects 2-7, separated by semicolons')
pressurePSI = MibScalar((1, 3, 6, 1, 4, 1, 32185, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: pressurePSI.setStatus('current')
if mibBuilder.loadTexts: pressurePSI.setDescription('Pressure, in PSI or mbar')
dutycycle = MibScalar((1, 3, 6, 1, 4, 1, 32185, 2, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: dutycycle.setStatus('current')
if mibBuilder.loadTexts: dutycycle.setDescription('Current duty cycle, in percent; --- if none available')
statusVars = MibScalar((1, 3, 6, 1, 4, 1, 32185, 2, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(6, 6)).setFixedLength(6)).setMaxAccess("readonly")
if mibBuilder.loadTexts: statusVars.setStatus('current')
if mibBuilder.loadTexts: statusVars.setDescription('Summary of the status of the unit. Is always 7 characters Character 1 is super-state: govering whole system, if this unit is a master S=slave (not a master) M=master; N=master but system off line D=director; D=director but system off line master: for redundant systems director: for increasing pumping capability Character 2 is major state: N=normal, S=standby, L=leaky Character 3 is environment: N=normal, C=cold, H=hot Character 4 is canister 1 condition: O=OK (ie dry), F=full (wet), U=unknown, D=dead Character 5 is canister 1 usage: I=idle, U=in use, R=regenerating Character 6 is canister 2 condition, as in character 4 Character 7 is canister 2 usage, as in character 5')
temperature = MibScalar((1, 3, 6, 1, 4, 1, 32185, 2, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: temperature.setStatus('current')
if mibBuilder.loadTexts: temperature.setDescription('Current temperature, in degrees F or C')
alarms = MibScalar((1, 3, 6, 1, 4, 1, 32185, 2, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(30, 30)).setFixedLength(30)).setMaxAccess("readonly")
if mibBuilder.loadTexts: alarms.setStatus('current')
if mibBuilder.loadTexts: alarms.setDescription("Current alarm conditions: is a list of them Each character has a - for no alarm, or an A or W if there is an alarm. A means alarm (serious), W means a warning (not so serious). Severity levels may later change. List of alarms: (later versions may add more): A1: Low pressure A2: High pressure W3: High duty cycle W4: High temperature W5: Low temperature W6: Unused A7: Canister 1 won't heat A8: Canister 1 won't cool A9: Canister 2 won't heat A10: Canister 2 won't cool A11: Unable to pressurize A12: Dew point alarm W13: Compressor timeout (for future use) W14: Communications error A15: Canister 1 thermistor bad A16: Canister 2 thermistor bad A17: Ambient thermistor bad A18: Overpressure A19: Bad calibrations in EEPROM A20: Bad limits in EEPROM A21: Short cycling A22: Pump shut down due to error condition")
compressorHours = MibScalar((1, 3, 6, 1, 4, 1, 32185, 2, 1, 7), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(30, 30)).setFixedLength(30)).setMaxAccess("readonly")
if mibBuilder.loadTexts: compressorHours.setStatus('current')
if mibBuilder.loadTexts: compressorHours.setDescription('Number of hours that the compressor has been running; resolution is tenths of an hour.')
majorState = MibScalar((1, 3, 6, 1, 4, 1, 32185, 2, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("online", 1), ("standby", 2), ("leaky", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: majorState.setStatus('current')
if mibBuilder.loadTexts: majorState.setDescription('Major state of the dehydrator. Online: currently pressurizing. Standby: not pressurizing. Leaky: shut down because of inability to pressurize.')
cycleTime = MibScalar((1, 3, 6, 1, 4, 1, 32185, 2, 1, 9), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cycleTime.setStatus('current')
if mibBuilder.loadTexts: cycleTime.setDescription('Time of last duty cycle in seconds; 0.0 means none available')
lowerLimit = MibScalar((1, 3, 6, 1, 4, 1, 32185, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lowerLimit.setStatus('current')
if mibBuilder.loadTexts: lowerLimit.setDescription('The pressure, in PSI or mbar, at which the unit starts to pump')
upperLimit = MibScalar((1, 3, 6, 1, 4, 1, 32185, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: upperLimit.setStatus('current')
if mibBuilder.loadTexts: upperLimit.setDescription('The pressure, in PSI or mbar, which the unit pressurizes to')
lowerAlarmLimit = MibScalar((1, 3, 6, 1, 4, 1, 32185, 2, 2, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: lowerAlarmLimit.setStatus('current')
if mibBuilder.loadTexts: lowerAlarmLimit.setDescription('The pressure, in PSI or mbar, below which the unit declares a low pressure alarm')
upperAlarmLimit = MibScalar((1, 3, 6, 1, 4, 1, 32185, 2, 2, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(10, 10)).setFixedLength(10)).setMaxAccess("readonly")
if mibBuilder.loadTexts: upperAlarmLimit.setStatus('current')
if mibBuilder.loadTexts: upperAlarmLimit.setDescription('The pressure, in PSI or mbar, above which the unit declares a high pressure alarm')
mibBuilder.exportSymbols("ADH-NETCOM-MIB", allStatuses=allStatuses, pressurePSI=pressurePSI, temperature=temperature, upperLimit=upperLimit, dutycycle=dutycycle, compressorHours=compressorHours, alarms=alarms, netcom=netcom, statusVars=statusVars, environmentalTechnology=environmentalTechnology, paramsInfo=paramsInfo, majorState=majorState, cycleTime=cycleTime, lowerLimit=lowerLimit, lowerAlarmLimit=lowerAlarmLimit, PYSNMP_MODULE_ID=environmentalTechnology, statusInfo=statusInfo, upperAlarmLimit=upperAlarmLimit)
