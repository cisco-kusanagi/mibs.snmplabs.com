#
# PySNMP MIB module ASCEND-MIBTHRESHHDSL2SHDSL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBTHRESHHDSL2SHDSL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:12:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, ModuleIdentity, Counter64, TimeTicks, Integer32, MibIdentifier, NotificationType, iso, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "ModuleIdentity", "Counter64", "TimeTicks", "Integer32", "MibIdentifier", "NotificationType", "iso", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibthreshHdsl2ShdslProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 160))
mibthreshHdsl2ShdslProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 160, 1), )
if mibBuilder.loadTexts: mibthreshHdsl2ShdslProfileTable.setStatus('mandatory')
mibthreshHdsl2ShdslProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1), ).setIndexNames((0, "ASCEND-MIBTHRESHHDSL2SHDSL-MIB", "threshHdsl2ShdslProfile-Name"))
if mibBuilder.loadTexts: mibthreshHdsl2ShdslProfileEntry.setStatus('mandatory')
threshHdsl2ShdslProfile_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 1), DisplayString()).setLabel("threshHdsl2ShdslProfile-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: threshHdsl2ShdslProfile_Name.setStatus('mandatory')
threshHdsl2ShdslProfile_LoopAttenuationThresh = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 2), Integer32()).setLabel("threshHdsl2ShdslProfile-LoopAttenuationThresh").setMaxAccess("readwrite")
if mibBuilder.loadTexts: threshHdsl2ShdslProfile_LoopAttenuationThresh.setStatus('mandatory')
threshHdsl2ShdslProfile_SnrMgnThresh = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 3), Integer32()).setLabel("threshHdsl2ShdslProfile-SnrMgnThresh").setMaxAccess("readwrite")
if mibBuilder.loadTexts: threshHdsl2ShdslProfile_SnrMgnThresh.setStatus('mandatory')
threshHdsl2ShdslProfile_ErroredSecondsThresh = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 4), Integer32()).setLabel("threshHdsl2ShdslProfile-ErroredSecondsThresh").setMaxAccess("readwrite")
if mibBuilder.loadTexts: threshHdsl2ShdslProfile_ErroredSecondsThresh.setStatus('mandatory')
threshHdsl2ShdslProfile_SeverelyErroredSecondsThresh = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 5), Integer32()).setLabel("threshHdsl2ShdslProfile-SeverelyErroredSecondsThresh").setMaxAccess("readwrite")
if mibBuilder.loadTexts: threshHdsl2ShdslProfile_SeverelyErroredSecondsThresh.setStatus('mandatory')
threshHdsl2ShdslProfile_CrcThresh = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 6), Integer32()).setLabel("threshHdsl2ShdslProfile-CrcThresh").setMaxAccess("readwrite")
if mibBuilder.loadTexts: threshHdsl2ShdslProfile_CrcThresh.setStatus('mandatory')
threshHdsl2ShdslProfile_LoswsThresh = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 7), Integer32()).setLabel("threshHdsl2ShdslProfile-LoswsThresh").setMaxAccess("readwrite")
if mibBuilder.loadTexts: threshHdsl2ShdslProfile_LoswsThresh.setStatus('mandatory')
threshHdsl2ShdslProfile_UasThresh = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 8), Integer32()).setLabel("threshHdsl2ShdslProfile-UasThresh").setMaxAccess("readwrite")
if mibBuilder.loadTexts: threshHdsl2ShdslProfile_UasThresh.setStatus('mandatory')
threshHdsl2ShdslProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 160, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("threshHdsl2ShdslProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: threshHdsl2ShdslProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBTHRESHHDSL2SHDSL-MIB", threshHdsl2ShdslProfile_ErroredSecondsThresh=threshHdsl2ShdslProfile_ErroredSecondsThresh, mibthreshHdsl2ShdslProfile=mibthreshHdsl2ShdslProfile, threshHdsl2ShdslProfile_LoopAttenuationThresh=threshHdsl2ShdslProfile_LoopAttenuationThresh, threshHdsl2ShdslProfile_CrcThresh=threshHdsl2ShdslProfile_CrcThresh, threshHdsl2ShdslProfile_Name=threshHdsl2ShdslProfile_Name, threshHdsl2ShdslProfile_LoswsThresh=threshHdsl2ShdslProfile_LoswsThresh, mibthreshHdsl2ShdslProfileEntry=mibthreshHdsl2ShdslProfileEntry, threshHdsl2ShdslProfile_SnrMgnThresh=threshHdsl2ShdslProfile_SnrMgnThresh, mibthreshHdsl2ShdslProfileTable=mibthreshHdsl2ShdslProfileTable, threshHdsl2ShdslProfile_Action_o=threshHdsl2ShdslProfile_Action_o, DisplayString=DisplayString, threshHdsl2ShdslProfile_SeverelyErroredSecondsThresh=threshHdsl2ShdslProfile_SeverelyErroredSecondsThresh, threshHdsl2ShdslProfile_UasThresh=threshHdsl2ShdslProfile_UasThresh)
