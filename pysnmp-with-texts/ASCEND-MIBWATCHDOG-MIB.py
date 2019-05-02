#
# PySNMP MIB module ASCEND-MIBWATCHDOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBWATCHDOG-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:28:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, iso, Counter32, Gauge32, ObjectIdentity, NotificationType, Counter64, Integer32, ModuleIdentity, Unsigned32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Counter32", "Gauge32", "ObjectIdentity", "NotificationType", "Counter64", "Integer32", "ModuleIdentity", "Unsigned32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibwatchdogConfigProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 162))
mibwatchdogConfigProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 162, 1), )
if mibBuilder.loadTexts: mibwatchdogConfigProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibwatchdogConfigProfileTable.setDescription('A list of mibwatchdogConfigProfile profile entries.')
mibwatchdogConfigProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1), ).setIndexNames((0, "ASCEND-MIBWATCHDOG-MIB", "watchdogConfigProfile-WatchdogIndex-WatchdogType"), (0, "ASCEND-MIBWATCHDOG-MIB", "watchdogConfigProfile-WatchdogIndex-LocationId"), (0, "ASCEND-MIBWATCHDOG-MIB", "watchdogConfigProfile-WatchdogIndex-Unit"))
if mibBuilder.loadTexts: mibwatchdogConfigProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibwatchdogConfigProfileEntry.setDescription('A mibwatchdogConfigProfile entry containing objects that maps to the parameters of mibwatchdogConfigProfile profile.')
watchdogConfigProfile_WatchdogIndex_WatchdogType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 1), Integer32()).setLabel("watchdogConfigProfile-WatchdogIndex-WatchdogType").setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogIndex_WatchdogType.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogIndex_WatchdogType.setDescription('A number that specifies the type of watchdog.')
watchdogConfigProfile_WatchdogIndex_LocationId = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 2), Integer32()).setLabel("watchdogConfigProfile-WatchdogIndex-LocationId").setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogIndex_LocationId.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogIndex_LocationId.setDescription('location id uniquely identifies the location of a watchdog')
watchdogConfigProfile_WatchdogIndex_Unit = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 3), Integer32()).setLabel("watchdogConfigProfile-WatchdogIndex-Unit").setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogIndex_Unit.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogIndex_Unit.setDescription('unit no specifies the instance no of a particular type of watchdog It is 1 based.')
watchdogConfigProfile_WatchdogTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("watchdogConfigProfile-WatchdogTrapEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogTrapEnable.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogTrapEnable.setDescription('Enables or disables trap for the specific watchdog. default is yes ')
watchdogConfigProfile_WatchdogName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 5), DisplayString()).setLabel("watchdogConfigProfile-WatchdogName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogName.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogName.setDescription('Contains a descriptive name for the watchdog. The watchdog-name is sent to the SNMP manager when the watchdog causes a trap.')
watchdogConfigProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("watchdogConfigProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: watchdogConfigProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: watchdogConfigProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBWATCHDOG-MIB", watchdogConfigProfile_WatchdogIndex_LocationId=watchdogConfigProfile_WatchdogIndex_LocationId, mibwatchdogConfigProfile=mibwatchdogConfigProfile, watchdogConfigProfile_WatchdogIndex_WatchdogType=watchdogConfigProfile_WatchdogIndex_WatchdogType, watchdogConfigProfile_WatchdogIndex_Unit=watchdogConfigProfile_WatchdogIndex_Unit, mibwatchdogConfigProfileTable=mibwatchdogConfigProfileTable, watchdogConfigProfile_Action_o=watchdogConfigProfile_Action_o, DisplayString=DisplayString, watchdogConfigProfile_WatchdogName=watchdogConfigProfile_WatchdogName, watchdogConfigProfile_WatchdogTrapEnable=watchdogConfigProfile_WatchdogTrapEnable, mibwatchdogConfigProfileEntry=mibwatchdogConfigProfileEntry)
