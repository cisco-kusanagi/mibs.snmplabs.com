#
# PySNMP MIB module ASCEND-MIBCALLSW-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBCALLSW-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Unsigned32, Gauge32, Counter32, ObjectIdentity, Integer32, Counter64, iso, TimeTicks, MibIdentifier, Bits, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Unsigned32", "Gauge32", "Counter32", "ObjectIdentity", "Integer32", "Counter64", "iso", "TimeTicks", "MibIdentifier", "Bits", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibcallSwitchingProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 65))
mibcallSwitchingProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 65, 1), )
if mibBuilder.loadTexts: mibcallSwitchingProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibcallSwitchingProfileTable.setDescription('A list of mibcallSwitchingProfile profile entries.')
mibcallSwitchingProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1), ).setIndexNames((0, "ASCEND-MIBCALLSW-MIB", "callSwitchingProfile-Index-o"))
if mibBuilder.loadTexts: mibcallSwitchingProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibcallSwitchingProfileEntry.setDescription('A mibcallSwitchingProfile entry containing objects that maps to the parameters of mibcallSwitchingProfile profile.')
callSwitchingProfile_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1, 1), Integer32()).setLabel("callSwitchingProfile-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: callSwitchingProfile_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: callSwitchingProfile_Index_o.setDescription('')
callSwitchingProfile_Enabled = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("callSwitchingProfile-Enabled").setMaxAccess("readwrite")
if mibBuilder.loadTexts: callSwitchingProfile_Enabled.setStatus('mandatory')
if mibBuilder.loadTexts: callSwitchingProfile_Enabled.setDescription("This flag controls whether to search CALL-ROUTE profiles to detect if an incoming call needs to be passed through or routed to network side. When the flag is set to 'no', such procedure will not be used.")
callSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("callSwitchingProfile-ComparisonRule-CallRouteEmptyPhoneNumberAcceptable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: callSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable.setStatus('mandatory')
if mibBuilder.loadTexts: callSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable.setDescription("This flag tells whether CALL-ROUTE profiles with empty phone numbers should be used in comparison. If the flag is set to 'yes', empty phone number in a CALL-ROUTE profile will match any dialed number.")
callSwitchingProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 65, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("callSwitchingProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: callSwitchingProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: callSwitchingProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBCALLSW-MIB", callSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable=callSwitchingProfile_ComparisonRule_CallRouteEmptyPhoneNumberAcceptable, mibcallSwitchingProfileEntry=mibcallSwitchingProfileEntry, DisplayString=DisplayString, mibcallSwitchingProfileTable=mibcallSwitchingProfileTable, callSwitchingProfile_Enabled=callSwitchingProfile_Enabled, callSwitchingProfile_Action_o=callSwitchingProfile_Action_o, mibcallSwitchingProfile=mibcallSwitchingProfile, callSwitchingProfile_Index_o=callSwitchingProfile_Index_o)
