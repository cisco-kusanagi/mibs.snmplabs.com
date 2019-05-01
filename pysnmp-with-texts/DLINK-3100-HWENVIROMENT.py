#
# PySNMP MIB module DLINK-3100-HWENVIROMENT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/DLINK-3100-HWENVIROMENT
# Produced by pysmi-0.3.4 at Wed May  1 12:48:27 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection")
rnd, = mibBuilder.importSymbols("DLINK-3100-MIB", "rnd")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, Counter32, ModuleIdentity, ObjectIdentity, TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Gauge32, Integer32, MibIdentifier, Unsigned32, Bits, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Counter32", "ModuleIdentity", "ObjectIdentity", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Gauge32", "Integer32", "MibIdentifier", "Unsigned32", "Bits", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlEnv = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 83))
rlEnv.setRevisions(('2003-09-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlEnv.setRevisionsDescriptions(('Added this MODULE-IDENTITY clause.',))
if mibBuilder.loadTexts: rlEnv.setLastUpdated('200309210000Z')
if mibBuilder.loadTexts: rlEnv.setOrganization('Dlink, Inc.')
if mibBuilder.loadTexts: rlEnv.setContactInfo('www.dlink.com')
if mibBuilder.loadTexts: rlEnv.setDescription('The private MIB module definition for environment of DLINK-3100 devices.')
class RlEnvMonState(TextualConvention, Integer32):
    description = 'Represents the state of a device being monitored. Valid values are: normal(1): the environment is good, such as low temperature. warning(2): the environment is bad, such as temperature above normal operation range but not too high. critical(3): the environment is very bad, such as temperature much higher than normal operation limit. shutdown(4): the environment is the worst, the system should be shutdown immediately. notPresent(5): the environmental monitor is not present, such as temperature sensors do not exist. notFunctioning(6): the environmental monitor does not function properly, such as a temperature sensor generates a abnormal data like 1000 C. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("normal", 1), ("warning", 2), ("critical", 3), ("shutdown", 4), ("notPresent", 5), ("notFunctioning", 6))

rlEnvPhysicalDescription = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 83, 1))
rlEnvMonFanStatusTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 83, 1, 1), )
if mibBuilder.loadTexts: rlEnvMonFanStatusTable.setStatus('current')
if mibBuilder.loadTexts: rlEnvMonFanStatusTable.setDescription('The table of fan status maintained by the environmental monitor.')
rlEnvMonFanStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 83, 1, 1, 1), ).setIndexNames((0, "DLINK-3100-HWENVIROMENT", "rlEnvMonFanStatusIndex"))
if mibBuilder.loadTexts: rlEnvMonFanStatusEntry.setStatus('current')
if mibBuilder.loadTexts: rlEnvMonFanStatusEntry.setDescription('An entry in the fan status table, representing the status of the associated fan maintained by the environmental monitor.')
rlEnvMonFanStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 83, 1, 1, 1, 1), Integer32())
if mibBuilder.loadTexts: rlEnvMonFanStatusIndex.setStatus('current')
if mibBuilder.loadTexts: rlEnvMonFanStatusIndex.setDescription('Unique index for the fan being instrumented. This index is for SNMP purposes only, and has no intrinsic meaning.')
rlEnvMonFanStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 83, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonFanStatusDescr.setStatus('current')
if mibBuilder.loadTexts: rlEnvMonFanStatusDescr.setDescription('Textual description of the fan being instrumented. This description is a short textual label, suitable as a human-sensible identification for the rest of the information in the entry.')
rlEnvMonFanState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 83, 1, 1, 1, 3), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonFanState.setStatus('current')
if mibBuilder.loadTexts: rlEnvMonFanState.setDescription('The mandatory state of the fan being instrumented.')
rlEnvMonSupplyStatusTable = MibTable((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 83, 1, 2), )
if mibBuilder.loadTexts: rlEnvMonSupplyStatusTable.setStatus('current')
if mibBuilder.loadTexts: rlEnvMonSupplyStatusTable.setDescription('The table of power supply status maintained by the environmental monitor card.')
rlEnvMonSupplyStatusEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 83, 1, 2, 1), ).setIndexNames((0, "DLINK-3100-HWENVIROMENT", "rlEnvMonSupplyStatusIndex"))
if mibBuilder.loadTexts: rlEnvMonSupplyStatusEntry.setStatus('current')
if mibBuilder.loadTexts: rlEnvMonSupplyStatusEntry.setDescription('An entry in the power supply status table, representing the status of the associated power supply maintained by the environmental monitor card.')
rlEnvMonSupplyStatusIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 83, 1, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647)))
if mibBuilder.loadTexts: rlEnvMonSupplyStatusIndex.setStatus('current')
if mibBuilder.loadTexts: rlEnvMonSupplyStatusIndex.setDescription('Unique index for the power supply being instrumented. This index is for SNMP purposes only, and has no intrinsic meaning.')
rlEnvMonSupplyStatusDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 83, 1, 2, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonSupplyStatusDescr.setStatus('current')
if mibBuilder.loadTexts: rlEnvMonSupplyStatusDescr.setDescription('Textual description of the power supply being instrumented. This description is a short textual label, suitable as a human-sensible identification for the rest of the information in the entry.')
rlEnvMonSupplyState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 83, 1, 2, 1, 3), RlEnvMonState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonSupplyState.setStatus('current')
if mibBuilder.loadTexts: rlEnvMonSupplyState.setDescription('The mandatory state of the power supply being instrumented.')
rlEnvMonSupplySource = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 83, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("unknown", 1), ("ac", 2), ("dc", 3), ("externalPowerSupply", 4), ("internalRedundant", 5)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlEnvMonSupplySource.setStatus('current')
if mibBuilder.loadTexts: rlEnvMonSupplySource.setDescription('The power supply source. unknown - Power supply source unknown ac - AC power supply dc - DC power supply externalPowerSupply - External power supply internalRedundant - Internal redundant power supply ')
mibBuilder.exportSymbols("DLINK-3100-HWENVIROMENT", rlEnvMonFanStatusIndex=rlEnvMonFanStatusIndex, rlEnvMonFanStatusEntry=rlEnvMonFanStatusEntry, rlEnvMonSupplyState=rlEnvMonSupplyState, rlEnv=rlEnv, rlEnvPhysicalDescription=rlEnvPhysicalDescription, rlEnvMonSupplySource=rlEnvMonSupplySource, rlEnvMonFanState=rlEnvMonFanState, rlEnvMonSupplyStatusIndex=rlEnvMonSupplyStatusIndex, rlEnvMonSupplyStatusDescr=rlEnvMonSupplyStatusDescr, RlEnvMonState=RlEnvMonState, rlEnvMonFanStatusTable=rlEnvMonFanStatusTable, rlEnvMonFanStatusDescr=rlEnvMonFanStatusDescr, rlEnvMonSupplyStatusTable=rlEnvMonSupplyStatusTable, PYSNMP_MODULE_ID=rlEnv, rlEnvMonSupplyStatusEntry=rlEnvMonSupplyStatusEntry)