#
# PySNMP MIB module DKSF-60-4-X-X-X (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DKSF-60-4-X-X-X
# Produced by pysmi-0.3.4 at Wed May  1 12:47:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
snmpTraps, = mibBuilder.importSymbols("SNMPv2-MIB", "snmpTraps")
Counter64, MibIdentifier, ObjectIdentity, enterprises, ModuleIdentity, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, IpAddress, Unsigned32, iso, Integer32, TimeTicks, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "ObjectIdentity", "enterprises", "ModuleIdentity", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "IpAddress", "Unsigned32", "iso", "Integer32", "TimeTicks", "NotificationType")
TextualConvention, TruthValue, DisplayString, TimeStamp = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TruthValue", "DisplayString", "TimeStamp")
netPing = ModuleIdentity((1, 3, 6, 1, 4, 1, 25728, 50))
netPing.setRevisions(('2014-11-21 00:00', '2014-10-23 00:00', '2012-10-09 00:00', '2012-03-01 00:00', '2011-04-11 00:00', '2011-02-05 00:00', '2011-01-28 00:00', '2010-04-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: netPing.setRevisionsDescriptions(('npRelayFlip variable max-access bugfix', 'Major update for DKSF 60.4', 'npTrapEmailTo variable is added in Traps for forwarding to email with external service', 'npReboot branch is added', 'npIoPulseCounter, npIoSinglePulseDuration, npIoSinglePulseStart is added Identification is changed from DKSF 52.3 to DKSF 52.4', 'npIoCurLoop Traps', "DKSF 50.9.1.A-2,-3,-10 - IR module (DKST28) support, new Trap definitions for npIO and npThermo. It's NO backward compatibility with DKSF 50.8 on Traps!", 'SMIv2-style rewrite',))
if mibBuilder.loadTexts: netPing.setLastUpdated('201411210000Z')
if mibBuilder.loadTexts: netPing.setOrganization('NetPing East, Alentis Electronics')
if mibBuilder.loadTexts: netPing.setContactInfo('developers@netping.ru')
if mibBuilder.loadTexts: netPing.setDescription('Generic MIB for NetPing remote sensing and control')
lightcom = MibIdentifier((1, 3, 6, 1, 4, 1, 25728))
npRelay = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 5500))
npRelayTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 5500, 5), )
if mibBuilder.loadTexts: npRelayTable.setStatus('current')
if mibBuilder.loadTexts: npRelayTable.setDescription('Watchdog and outlet/relay control table')
npRelayEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1), ).setIndexNames((0, "DKSF-60-4-X-X-X", "npRelayN"))
if mibBuilder.loadTexts: npRelayEntry.setStatus('current')
if mibBuilder.loadTexts: npRelayEntry.setDescription('Relay/outlet table row')
npRelayN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayN.setStatus('current')
if mibBuilder.loadTexts: npRelayN.setDescription('The N of output relay')
npRelayMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("watchdog", 2), ("schedule", 3), ("scheduleAndWatchdog", 4), ("logic", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npRelayMode.setStatus('current')
if mibBuilder.loadTexts: npRelayMode.setDescription('Control of relay: 0 - manual off 1 - manual on 2 - watchdog 3 - schedule 4 - both schedule and watchdog (while switched on by schedule) 5 - logic')
npRelayStartReset = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npRelayStartReset.setStatus('current')
if mibBuilder.loadTexts: npRelayStartReset.setDescription('Write 1 to start reset (switch relay off for some time)')
npRelayMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayMemo.setStatus('current')
if mibBuilder.loadTexts: npRelayMemo.setDescription('Relay memo')
npRelayFlip = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1))).clone(namedValues=NamedValues(("flip", -1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npRelayFlip.setStatus('current')
if mibBuilder.loadTexts: npRelayFlip.setDescription('Write -1 to flip between manual on and manual off states of relay')
npRelayState = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5500, 5, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelayState.setStatus('current')
if mibBuilder.loadTexts: npRelayState.setDescription('Actual relay state at the moment, regardless of source of control. 0 - relay is off 1 - relay is on')
npPwr = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 5800))
npPwrTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 5800, 3), )
if mibBuilder.loadTexts: npPwrTable.setStatus('current')
if mibBuilder.loadTexts: npPwrTable.setDescription('Watchdog and outlet/relay control table')
npPwrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1), ).setIndexNames((0, "DKSF-60-4-X-X-X", "npPwrChannelN"))
if mibBuilder.loadTexts: npPwrEntry.setStatus('current')
if mibBuilder.loadTexts: npPwrEntry.setDescription('Watchdog and outlet/relay control table row')
npPwrChannelN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npPwrChannelN.setStatus('current')
if mibBuilder.loadTexts: npPwrChannelN.setDescription('The id of watchdog/power channel')
npPwrStartReset = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npPwrStartReset.setStatus('current')
if mibBuilder.loadTexts: npPwrStartReset.setDescription('Write 1 to start forced reset On read: 0 - normal operation 1 - reset is active 2 - reboot pause is active or watchdog is inactive')
npPwrManualMode = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("watchdog", 2), ("schedule", 3), ("scheduleAndWatchdog", 4), ("logic", 5)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npPwrManualMode.setStatus('current')
if mibBuilder.loadTexts: npPwrManualMode.setDescription('Mode of power channel 0 - manual off 1 - manual on 2 - watchdog 3 - schedule 4 - schedule and watchdog 5 - controlled by Logic')
npPwrResetsCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npPwrResetsCounter.setStatus('current')
if mibBuilder.loadTexts: npPwrResetsCounter.setDescription('Counter of watchdog resets Write 0 to clear.')
npPwrRepeatingResetsCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npPwrRepeatingResetsCounter.setStatus('current')
if mibBuilder.loadTexts: npPwrRepeatingResetsCounter.setDescription('Counter of continous failed watchdog resets')
npPwrMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npPwrMemo.setStatus('current')
if mibBuilder.loadTexts: npPwrMemo.setDescription('Relay channel memo')
npPwrRelayFlip = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 14), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(-1))).clone(namedValues=NamedValues(("flip", -1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npPwrRelayFlip.setStatus('current')
if mibBuilder.loadTexts: npPwrRelayFlip.setDescription('Write -1 to flip between manual on and manual off states of relay')
npPwrRelayState = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 5800, 3, 1, 15), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npPwrRelayState.setStatus('current')
if mibBuilder.loadTexts: npPwrRelayState.setDescription('Actual relay state at the moment, regardless of source of control. 0 - relay is off 1 - relay is on')
npThermo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800))
npThermoTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8800, 1), )
if mibBuilder.loadTexts: npThermoTable.setStatus('current')
if mibBuilder.loadTexts: npThermoTable.setDescription('Thermo Sensors Table')
npThermoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1), ).setIndexNames((0, "DKSF-60-4-X-X-X", "npThermoSensorN"))
if mibBuilder.loadTexts: npThermoEntry.setStatus('current')
if mibBuilder.loadTexts: npThermoEntry.setDescription('Thermo Sensors Table Row')
npThermoSensorN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoSensorN.setStatus('current')
if mibBuilder.loadTexts: npThermoSensorN.setDescription('The id of temperature sensor, 1 to 8')
npThermoValue = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoValue.setStatus('current')
if mibBuilder.loadTexts: npThermoValue.setDescription('Temperature, deg.C')
npThermoStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("failed", 0), ("low", 1), ("norm", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoStatus.setStatus('current')
if mibBuilder.loadTexts: npThermoStatus.setDescription('Temperature status (0=fault, 1=underheat, 2=normal, 3=overheat)')
npThermoLow = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoLow.setStatus('current')
if mibBuilder.loadTexts: npThermoLow.setDescription('Bottom margin of normal temperature range, deg.C')
npThermoHigh = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoHigh.setStatus('current')
if mibBuilder.loadTexts: npThermoHigh.setDescription('Top margin of normal temperature range, deg.C')
npThermoMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8800, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoMemo.setStatus('current')
if mibBuilder.loadTexts: npThermoMemo.setDescription('T channel memo')
npThermoTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800, 2))
npThermoTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0))
npThermoTrapSensorN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapSensorN.setStatus('current')
if mibBuilder.loadTexts: npThermoTrapSensorN.setDescription('The id of temperature sensor, 1 to 8')
npThermoTrapValue = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapValue.setStatus('current')
if mibBuilder.loadTexts: npThermoTrapValue.setDescription('Temperature, deg.C')
npThermoTrapStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("failed", 0), ("low", 1), ("norm", 2), ("high", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapStatus.setStatus('current')
if mibBuilder.loadTexts: npThermoTrapStatus.setDescription('Temperature status (0=fault, 1=underheat, 2=normal, 3=overheat)')
npThermoTrapLow = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapLow.setStatus('current')
if mibBuilder.loadTexts: npThermoTrapLow.setDescription('Bottom margin of normal temperature range, deg.C')
npThermoTrapHigh = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 280))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapHigh.setStatus('current')
if mibBuilder.loadTexts: npThermoTrapHigh.setDescription('Top margin of normal temperature range, deg.C')
npThermoTrapMemo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npThermoTrapMemo.setStatus('current')
if mibBuilder.loadTexts: npThermoTrapMemo.setDescription('T channel memo')
npThermoTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8800, 2, 0, 1)).setObjects(("DKSF-60-4-X-X-X", "npThermoTrapSensorN"), ("DKSF-60-4-X-X-X", "npThermoTrapValue"), ("DKSF-60-4-X-X-X", "npThermoTrapStatus"), ("DKSF-60-4-X-X-X", "npThermoTrapLow"), ("DKSF-60-4-X-X-X", "npThermoTrapHigh"), ("DKSF-60-4-X-X-X", "npThermoTrapMemo"))
if mibBuilder.loadTexts: npThermoTrap.setStatus('current')
if mibBuilder.loadTexts: npThermoTrap.setDescription('Status of Thermo sensor is changed (crossing of normal temp. range)')
npIo = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900))
npIoTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8900, 1), )
if mibBuilder.loadTexts: npIoTable.setStatus('current')
if mibBuilder.loadTexts: npIoTable.setDescription('Digital Input/output Table')
npIoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1), ).setIndexNames((0, "DKSF-60-4-X-X-X", "npIoLineN"))
if mibBuilder.loadTexts: npIoEntry.setStatus('current')
if mibBuilder.loadTexts: npIoEntry.setDescription('Digital Input/output Table Row')
npIoLineN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoLineN.setStatus('current')
if mibBuilder.loadTexts: npIoLineN.setDescription('Number of IO line, from 1 to max supported')
npIoLevelIn = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoLevelIn.setStatus('current')
if mibBuilder.loadTexts: npIoLevelIn.setDescription('Input level, 0 or 1')
npIoLevelOut = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoLevelOut.setStatus('current')
if mibBuilder.loadTexts: npIoLevelOut.setDescription('Output level, 0 or 1. Write -1 to flip output.')
npIoMemo = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoMemo.setStatus('current')
if mibBuilder.loadTexts: npIoMemo.setDescription('IO line memo')
npIoPulseCounter = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 9), Counter32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoPulseCounter.setStatus('current')
if mibBuilder.loadTexts: npIoPulseCounter.setDescription('Pulse Counter on IO input line (counts positive fronts) Write 0 to reset.')
npIoSinglePulseDuration = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 12), Integer32().subtype(subtypeSpec=ValueRangeConstraint(100, 25500))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoSinglePulseDuration.setStatus('current')
if mibBuilder.loadTexts: npIoSinglePulseDuration.setDescription('Set duration of single pulse on IO output line, 100ms to 25500ms, min. step is 100ms')
npIoSinglePulseStart = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8900, 1, 1, 13), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIoSinglePulseStart.setStatus('current')
if mibBuilder.loadTexts: npIoSinglePulseStart.setDescription('Write 1 to start single pulse on IO output. Output will be inverted for time, specified by npIoSinglePulseDuration')
npIoTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900, 2))
npIoTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0))
npIoTrapLineN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLineN.setStatus('current')
if mibBuilder.loadTexts: npIoTrapLineN.setDescription('Trap data, Number of IO line')
npIoTrapLevelIn = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapLevelIn.setStatus('current')
if mibBuilder.loadTexts: npIoTrapLevelIn.setDescription('Trap data, new Input level, 0 or 1')
npIoTrapMemo = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 6), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIoTrapMemo.setStatus('current')
if mibBuilder.loadTexts: npIoTrapMemo.setDescription('Trap data, IO line memo')
npIoTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8900, 2, 0, 1)).setObjects(("DKSF-60-4-X-X-X", "npIoTrapLineN"), ("DKSF-60-4-X-X-X", "npIoTrapLevelIn"), ("DKSF-60-4-X-X-X", "npIoTrapMemo"))
if mibBuilder.loadTexts: npIoTrap.setStatus('current')
if mibBuilder.loadTexts: npIoTrap.setDescription('Input state of IO line is changed')
npCurLoop = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8300))
npCurLoopTable = MibTable((1, 3, 6, 1, 4, 1, 25728, 8300, 1), )
if mibBuilder.loadTexts: npCurLoopTable.setStatus('current')
if mibBuilder.loadTexts: npCurLoopTable.setDescription('Current loop sensors Table')
npCurLoopEntry = MibTableRow((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1), ).setIndexNames((0, "DKSF-60-4-X-X-X", "npCurLoopN"))
if mibBuilder.loadTexts: npCurLoopEntry.setStatus('current')
if mibBuilder.loadTexts: npCurLoopEntry.setDescription('Current loop sensors Table Row')
npCurLoopN = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopN.setStatus('current')
if mibBuilder.loadTexts: npCurLoopN.setDescription('Index of current loop, 1 to max supported')
npCurLoopStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("ok", 0), ("alert", 1), ("cut", 2), ("short", 3), ("notPowered", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopStatus.setStatus('current')
if mibBuilder.loadTexts: npCurLoopStatus.setDescription('Status of the loop 0=Normal, 1=Alert, 2=Cut, 3=Short, 4=Not Powered')
npCurLoopI = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopI.setStatus('current')
if mibBuilder.loadTexts: npCurLoopI.setDescription('Loop current, mA')
npCurLoopV = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopV.setStatus('current')
if mibBuilder.loadTexts: npCurLoopV.setDescription('Voltage drop on the loop, mV')
npCurLoopR = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopR.setStatus('current')
if mibBuilder.loadTexts: npCurLoopR.setDescription('Resistance of the loop, Ohm')
npCurLoopPower = MibTableColumn((1, 3, 6, 1, 4, 1, 25728, 8300, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("off", 0), ("on", 1), ("cyclePower", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npCurLoopPower.setStatus('current')
if mibBuilder.loadTexts: npCurLoopPower.setDescription('Control of loop power 0=Off, 1=On, 2=reset by off/on power')
npCurLoopTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8300, 2))
npCurLoopTrapPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 0))
npCurLoopTrapN = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapN.setStatus('current')
if mibBuilder.loadTexts: npCurLoopTrapN.setDescription('Index of current loop, which status has changed')
npCurLoopTrapStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))).clone(namedValues=NamedValues(("ok", 0), ("alert", 1), ("cut", 2), ("short", 3), ("notPowered", 4)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapStatus.setStatus('current')
if mibBuilder.loadTexts: npCurLoopTrapStatus.setDescription('Status of the loop 0=Normal, 1=Alert, 2=Cut, 3=Short, 4=Not Powered')
npCurLoopTrapI = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapI.setStatus('current')
if mibBuilder.loadTexts: npCurLoopTrapI.setDescription('Loop current, mA')
npCurLoopTrapV = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapV.setStatus('current')
if mibBuilder.loadTexts: npCurLoopTrapV.setDescription('Voltage drop on the loop, mV')
npCurLoopTrapR = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 99999))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npCurLoopTrapR.setStatus('current')
if mibBuilder.loadTexts: npCurLoopTrapR.setDescription('Resistance of the loop, Ohm')
npCurLoopTrapPower = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("off", 0), ("on", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npCurLoopTrapPower.setStatus('current')
if mibBuilder.loadTexts: npCurLoopTrapPower.setDescription('Status of loop power 0=Off, 1=On')
npCurLoopTrap = NotificationType((1, 3, 6, 1, 4, 1, 25728, 8300, 2, 0, 1)).setObjects(("DKSF-60-4-X-X-X", "npCurLoopTrapN"), ("DKSF-60-4-X-X-X", "npCurLoopTrapStatus"), ("DKSF-60-4-X-X-X", "npCurLoopTrapI"), ("DKSF-60-4-X-X-X", "npCurLoopTrapV"), ("DKSF-60-4-X-X-X", "npCurLoopTrapR"), ("DKSF-60-4-X-X-X", "npCurLoopTrapPower"))
if mibBuilder.loadTexts: npCurLoopTrap.setStatus('current')
if mibBuilder.loadTexts: npCurLoopTrap.setDescription('Status of current loop N has changed!')
npRelHumidity = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400))
npRelHumSensor = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 8400, 2))
npRelHumSensorStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("error", 0), ("ok", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorStatus.setStatus('current')
if mibBuilder.loadTexts: npRelHumSensorStatus.setDescription("Status of the Rel.Humidity Sensor One 0=Normal, 1=Error or Sensor isn't connected")
npRelHumSensorValueH = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorValueH.setStatus('current')
if mibBuilder.loadTexts: npRelHumSensorValueH.setDescription('Relative humidity value, %')
npRelHumSensorValueT = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(-60, 200))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorValueT.setStatus('current')
if mibBuilder.loadTexts: npRelHumSensorValueT.setDescription('Sensor temperature, deg.C')
npRelHumSensorStatusH = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))).clone(namedValues=NamedValues(("sensorFailed", 0), ("belowSafeRange", 1), ("inSafeRange", 2), ("aboveSafeRange", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorStatusH.setStatus('current')
if mibBuilder.loadTexts: npRelHumSensorStatusH.setDescription('Status of Relative Humiduty')
npRelHumSafeRangeHigh = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSafeRangeHigh.setStatus('current')
if mibBuilder.loadTexts: npRelHumSafeRangeHigh.setDescription('Relative Humidity safe range, top margin, %RH')
npRelHumSafeRangeLow = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 8), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 100))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSafeRangeLow.setStatus('current')
if mibBuilder.loadTexts: npRelHumSafeRangeLow.setDescription('Relative Humidity safe range, bottom margin, %RH')
npRelHumSensorValueT100 = MibScalar((1, 3, 6, 1, 4, 1, 25728, 8400, 2, 9), Integer32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: npRelHumSensorValueT100.setStatus('current')
if mibBuilder.loadTexts: npRelHumSensorValueT100.setDescription('Sensor temperature, deg.C * 100 (fixed point two decimal places) Used to get access to the fractional part of T value')
npIr = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 7900))
npIrCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 7900, 1))
npIrPlayCmd = MibScalar((1, 3, 6, 1, 4, 1, 25728, 7900, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIrPlayCmd.setStatus('current')
if mibBuilder.loadTexts: npIrPlayCmd.setDescription('Write IR command number to send IR command')
npIrReset = MibScalar((1, 3, 6, 1, 4, 1, 25728, 7900, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 1))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npIrReset.setStatus('current')
if mibBuilder.loadTexts: npIrReset.setDescription('Write 1 to reset IR transiever. After reset, send IR command and check npIrStatus.')
npIrStatus = MibScalar((1, 3, 6, 1, 4, 1, 25728, 7900, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 255))).clone(namedValues=NamedValues(("ok", 0), ("busyCaptureWaitingButton", 1), ("busyCaptureWaitingIr", 2), ("busyPlayback", 3), ("error", 255)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: npIrStatus.setStatus('current')
if mibBuilder.loadTexts: npIrStatus.setDescription('IR transiever status')
npReboot = MibIdentifier((1, 3, 6, 1, 4, 1, 25728, 911))
npSoftReboot = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npSoftReboot.setStatus('current')
if mibBuilder.loadTexts: npSoftReboot.setDescription('Write 1 to reboot device after current operations completition')
npResetStack = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npResetStack.setStatus('current')
if mibBuilder.loadTexts: npResetStack.setDescription('Write 1 to re-initialize network stack')
npForcedReboot = MibScalar((1, 3, 6, 1, 4, 1, 25728, 911, 3), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: npForcedReboot.setStatus('current')
if mibBuilder.loadTexts: npForcedReboot.setDescription('Write 1 to immediate forced reboot')
mibBuilder.exportSymbols("DKSF-60-4-X-X-X", npCurLoopTrap=npCurLoopTrap, npThermoSensorN=npThermoSensorN, npCurLoopV=npCurLoopV, npIoSinglePulseStart=npIoSinglePulseStart, npIoSinglePulseDuration=npIoSinglePulseDuration, npCurLoop=npCurLoop, npRelayTable=npRelayTable, npRelHumSensorValueH=npRelHumSensorValueH, npIr=npIr, npCurLoopTrapN=npCurLoopTrapN, npIoTrap=npIoTrap, npIo=npIo, npIrCtrl=npIrCtrl, npRelHumSensorStatusH=npRelHumSensorStatusH, npThermoTable=npThermoTable, npRelHumSafeRangeLow=npRelHumSafeRangeLow, npPwr=npPwr, npThermoTrapHigh=npThermoTrapHigh, npPwrManualMode=npPwrManualMode, npCurLoopEntry=npCurLoopEntry, npPwrEntry=npPwrEntry, npRelHumSensor=npRelHumSensor, npPwrResetsCounter=npPwrResetsCounter, npPwrRelayFlip=npPwrRelayFlip, npRelHumSensorStatus=npRelHumSensorStatus, npRelayState=npRelayState, npCurLoopTable=npCurLoopTable, npPwrTable=npPwrTable, npCurLoopTrapStatus=npCurLoopTrapStatus, npCurLoopStatus=npCurLoopStatus, npCurLoopN=npCurLoopN, npThermoValue=npThermoValue, npRelay=npRelay, npRelayN=npRelayN, npPwrRepeatingResetsCounter=npPwrRepeatingResetsCounter, npThermoTrap=npThermoTrap, npIoEntry=npIoEntry, npRelayFlip=npRelayFlip, npThermoTrapLow=npThermoTrapLow, npThermoTrapValue=npThermoTrapValue, npPwrStartReset=npPwrStartReset, npRelHumSensorValueT=npRelHumSensorValueT, npPwrChannelN=npPwrChannelN, npThermoTrapSensorN=npThermoTrapSensorN, npCurLoopTrapR=npCurLoopTrapR, npCurLoopI=npCurLoopI, npIoTable=npIoTable, npCurLoopPower=npCurLoopPower, npCurLoopTrapPrefix=npCurLoopTrapPrefix, lightcom=lightcom, PYSNMP_MODULE_ID=netPing, npIoLevelIn=npIoLevelIn, npThermoTraps=npThermoTraps, npCurLoopTraps=npCurLoopTraps, npIoTrapLineN=npIoTrapLineN, npPwrMemo=npPwrMemo, npSoftReboot=npSoftReboot, npCurLoopR=npCurLoopR, npRelHumidity=npRelHumidity, npIoTrapPrefix=npIoTrapPrefix, npIoTrapMemo=npIoTrapMemo, npThermoLow=npThermoLow, netPing=netPing, npForcedReboot=npForcedReboot, npRelayMemo=npRelayMemo, npRelHumSafeRangeHigh=npRelHumSafeRangeHigh, npIoTrapLevelIn=npIoTrapLevelIn, npIoPulseCounter=npIoPulseCounter, npThermoEntry=npThermoEntry, npIrPlayCmd=npIrPlayCmd, npRelayStartReset=npRelayStartReset, npThermoHigh=npThermoHigh, npIoLineN=npIoLineN, npCurLoopTrapPower=npCurLoopTrapPower, npThermoTrapMemo=npThermoTrapMemo, npThermoMemo=npThermoMemo, npIoLevelOut=npIoLevelOut, npIoTraps=npIoTraps, npIoMemo=npIoMemo, npPwrRelayState=npPwrRelayState, npThermoStatus=npThermoStatus, npCurLoopTrapV=npCurLoopTrapV, npIrStatus=npIrStatus, npReboot=npReboot, npRelayEntry=npRelayEntry, npResetStack=npResetStack, npRelayMode=npRelayMode, npIrReset=npIrReset, npCurLoopTrapI=npCurLoopTrapI, npRelHumSensorValueT100=npRelHumSensorValueT100, npThermo=npThermo, npThermoTrapPrefix=npThermoTrapPrefix, npThermoTrapStatus=npThermoTrapStatus)
