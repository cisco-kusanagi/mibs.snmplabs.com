#
# PySNMP MIB module ASCEND-MIBCALLSW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBCALLSW-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, Gauge32, Counter32, Bits, Integer32, Counter64, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ObjectIdentity, iso, IpAddress, ModuleIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "Counter32", "Bits", "Integer32", "Counter64", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ObjectIdentity", "iso", "IpAddress", "ModuleIdentity", "MibIdentifier")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibcallSwitchingProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 65))
mibcallSwitchingProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 65, 1), )
if mibBuilder.loadTexts: mibcallSwitchingProfileTable.setStatus('mandatory')
mibcallSwitchingProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1), ).setIndexNames((0, "ASCEND-MIBCALLSW-MIB", "callSwitchingProfile-Index-o"))
if mibBuilder.loadTexts: mibcallSwitchingProfileEntry.setStatus('mandatory')
callSwitchingProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1, 1), Integer32()).setLabel("callSwitchingProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: callSwitchingProfile_Index_o.setStatus('mandatory')
callSwitchingProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("callSwitchingProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: callSwitchingProfile_Enabled.setStatus('mandatory')
callSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("callSwitchingProfile-ComparisonRule-CallRouteEmptyPhoneNumberAcceptable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: callSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable.setStatus('mandatory')
callSwitchingProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("callSwitchingProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: callSwitchingProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBCALLSW-MIB", callSwitchingProfile_Enabled=callSwitchingProfile_Enabled, mibcallSwitchingProfileEntry=mibcallSwitchingProfileEntry, callSwitchingProfile_Index_o=callSwitchingProfile_Index_o, callSwitchingProfile_Action_o=callSwitchingProfile_Action_o, mibcallSwitchingProfile=mibcallSwitchingProfile, DisplayString=DisplayString, callSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable=callSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable, mibcallSwitchingProfileTable=mibcallSwitchingProfileTable)
