#
# PySNMP MIB module ASCEND-MIBWATCHDOG-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBWATCHDOG-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, Bits, Unsigned32, Counter64, ObjectIdentity, iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Counter32, MibIdentifier, Gauge32, TimeTicks, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Bits", "Unsigned32", "Counter64", "ObjectIdentity", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Counter32", "MibIdentifier", "Gauge32", "TimeTicks", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibwatchdogConfigProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 162))
mibwatchdogConfigProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 162, 1), )
if mibBuilder.loadTexts: mibwatchdogConfigProfileTable.setStatus('mandatory')
mibwatchdogConfigProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1), ).setIndexNames((0, "ASCEND-MIBWATCHDOG-MIB", "watchdogConfigProfile-WatchdogIndex-WatchdogType"), (0, "ASCEND-MIBWATCHDOG-MIB", "watchdogConfigProfile-WatchdogIndex-LocationId"), (0, "ASCEND-MIBWATCHDOG-MIB", "watchdogConfigProfile-WatchdogIndex-Unit"))
if mibBuilder.loadTexts: mibwatchdogConfigProfileEntry.setStatus('mandatory')
watchdogConfigProfile_WatchdogIndex_WatchdogType = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 1), Integer32()).setLabel("watchdogConfigProfile-WatchdogIndex-WatchdogType").setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogIndex_WatchdogType.setStatus('mandatory')
watchdogConfigProfile_WatchdogIndex_LocationId = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 2), Integer32()).setLabel("watchdogConfigProfile-WatchdogIndex-LocationId").setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogIndex_LocationId.setStatus('mandatory')
watchdogConfigProfile_WatchdogIndex_Unit = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 3), Integer32()).setLabel("watchdogConfigProfile-WatchdogIndex-Unit").setMaxAccess("readonly")
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogIndex_Unit.setStatus('mandatory')
watchdogConfigProfile_WatchdogTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("watchdogConfigProfile-WatchdogTrapEnable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogTrapEnable.setStatus('mandatory')
watchdogConfigProfile_WatchdogName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 5), DisplayString()).setLabel("watchdogConfigProfile-WatchdogName").setMaxAccess("readwrite")
if mibBuilder.loadTexts: watchdogConfigProfile_WatchdogName.setStatus('mandatory')
watchdogConfigProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 162, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("watchdogConfigProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: watchdogConfigProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBWATCHDOG-MIB", mibwatchdogConfigProfile=mibwatchdogConfigProfile, mibwatchdogConfigProfileEntry=mibwatchdogConfigProfileEntry, watchdogConfigProfile_WatchdogName=watchdogConfigProfile_WatchdogName, watchdogConfigProfile_WatchdogIndex_Unit=watchdogConfigProfile_WatchdogIndex_Unit, mibwatchdogConfigProfileTable=mibwatchdogConfigProfileTable, watchdogConfigProfile_WatchdogTrapEnable=watchdogConfigProfile_WatchdogTrapEnable, watchdogConfigProfile_WatchdogIndex_LocationId=watchdogConfigProfile_WatchdogIndex_LocationId, DisplayString=DisplayString, watchdogConfigProfile_Action_o=watchdogConfigProfile_Action_o, watchdogConfigProfile_WatchdogIndex_WatchdogType=watchdogConfigProfile_WatchdogIndex_WatchdogType)
