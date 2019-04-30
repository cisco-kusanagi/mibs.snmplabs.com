#
# PySNMP MIB module ASCEND-MIBDS1CLKERR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBDS1CLKERR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:11:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, IpAddress, TimeTicks, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter64, ObjectIdentity, ModuleIdentity, MibIdentifier, Integer32, Counter32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "IpAddress", "TimeTicks", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter64", "ObjectIdentity", "ModuleIdentity", "MibIdentifier", "Integer32", "Counter32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibds1ClockErrorProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 164))
mibds1ClockErrorProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 164, 1), )
if mibBuilder.loadTexts: mibds1ClockErrorProfileTable.setStatus('mandatory')
mibds1ClockErrorProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1), ).setIndexNames((0, "ASCEND-MIBDS1CLKERR-MIB", "ds1ClockErrorProfile-Index-o"))
if mibBuilder.loadTexts: mibds1ClockErrorProfileEntry.setStatus('mandatory')
ds1ClockErrorProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 1), Integer32()).setLabel("ds1ClockErrorProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: ds1ClockErrorProfile_Index_o.setStatus('mandatory')
ds1ClockErrorProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("ds1ClockErrorProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_Enabled.setStatus('mandatory')
ds1ClockErrorProfile_CrcThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 3), Integer32()).setLabel("ds1ClockErrorProfile-CrcThreshold").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_CrcThreshold.setStatus('mandatory')
ds1ClockErrorProfile_FrameSlipsThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 4), Integer32()).setLabel("ds1ClockErrorProfile-FrameSlipsThreshold").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_FrameSlipsThreshold.setStatus('mandatory')
ds1ClockErrorProfile_FerThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 5), Integer32()).setLabel("ds1ClockErrorProfile-FerThreshold").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_FerThreshold.setStatus('mandatory')
ds1ClockErrorProfile_OofThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 6), Integer32()).setLabel("ds1ClockErrorProfile-OofThreshold").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_OofThreshold.setStatus('mandatory')
ds1ClockErrorProfile_FebeThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 7), Integer32()).setLabel("ds1ClockErrorProfile-FebeThreshold").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_FebeThreshold.setStatus('mandatory')
ds1ClockErrorProfile_LcvThreshold = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 8), Integer32()).setLabel("ds1ClockErrorProfile-LcvThreshold").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_LcvThreshold.setStatus('mandatory')
ds1ClockErrorProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 164, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("ds1ClockErrorProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: ds1ClockErrorProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBDS1CLKERR-MIB", ds1ClockErrorProfile_Index_o=ds1ClockErrorProfile_Index_o, ds1ClockErrorProfile_CrcThreshold=ds1ClockErrorProfile_CrcThreshold, ds1ClockErrorProfile_FrameSlipsThreshold=ds1ClockErrorProfile_FrameSlipsThreshold, ds1ClockErrorProfile_FebeThreshold=ds1ClockErrorProfile_FebeThreshold, mibds1ClockErrorProfileTable=mibds1ClockErrorProfileTable, DisplayString=DisplayString, ds1ClockErrorProfile_Enabled=ds1ClockErrorProfile_Enabled, ds1ClockErrorProfile_FerThreshold=ds1ClockErrorProfile_FerThreshold, ds1ClockErrorProfile_OofThreshold=ds1ClockErrorProfile_OofThreshold, ds1ClockErrorProfile_LcvThreshold=ds1ClockErrorProfile_LcvThreshold, ds1ClockErrorProfile_Action_o=ds1ClockErrorProfile_Action_o, mibds1ClockErrorProfile=mibds1ClockErrorProfile, mibds1ClockErrorProfileEntry=mibds1ClockErrorProfileEntry)
