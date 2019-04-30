#
# PySNMP MIB module ASCEND-MIBATMPREFIX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBATMPREFIX-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Integer32, NotificationType, IpAddress, Counter32, ModuleIdentity, iso, Counter64, Bits, TimeTicks, Gauge32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Integer32", "NotificationType", "IpAddress", "Counter32", "ModuleIdentity", "iso", "Counter64", "Bits", "TimeTicks", "Gauge32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibatmPrefixProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 22))
mibatmPrefixProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 22, 1), )
if mibBuilder.loadTexts: mibatmPrefixProfileTable.setStatus('mandatory')
mibatmPrefixProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1), ).setIndexNames((0, "ASCEND-MIBATMPREFIX-MIB", "atmPrefixProfile-PrefixName"))
if mibBuilder.loadTexts: mibatmPrefixProfileEntry.setStatus('mandatory')
atmPrefixProfile_PrefixName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 1), DisplayString()).setLabel("atmPrefixProfile-PrefixName").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmPrefixProfile_PrefixName.setStatus('mandatory')
atmPrefixProfile_UseShortAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("atmPrefixProfile-UseShortAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPrefixProfile_UseShortAddress.setStatus('mandatory')
atmPrefixProfile_PnniNodePrefix_Length = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 3), Integer32()).setLabel("atmPrefixProfile-PnniNodePrefix-Length").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPrefixProfile_PnniNodePrefix_Length.setStatus('mandatory')
atmPrefixProfile_PnniNodePrefix_Address = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 4), DisplayString()).setLabel("atmPrefixProfile-PnniNodePrefix-Address").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPrefixProfile_PnniNodePrefix_Address.setStatus('mandatory')
atmPrefixProfile_SpvcAddressPrefix_Length = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 5), Integer32()).setLabel("atmPrefixProfile-SpvcAddressPrefix-Length").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPrefixProfile_SpvcAddressPrefix_Length.setStatus('mandatory')
atmPrefixProfile_SpvcAddressPrefix_Address = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 6), DisplayString()).setLabel("atmPrefixProfile-SpvcAddressPrefix-Address").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPrefixProfile_SpvcAddressPrefix_Address.setStatus('mandatory')
atmPrefixProfile_SvcAddressPrefix_Length = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 7), Integer32()).setLabel("atmPrefixProfile-SvcAddressPrefix-Length").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPrefixProfile_SvcAddressPrefix_Length.setStatus('mandatory')
atmPrefixProfile_SvcAddressPrefix_Address = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 8), DisplayString()).setLabel("atmPrefixProfile-SvcAddressPrefix-Address").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPrefixProfile_SvcAddressPrefix_Address.setStatus('mandatory')
atmPrefixProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 22, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("atmPrefixProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmPrefixProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBATMPREFIX-MIB", mibatmPrefixProfile=mibatmPrefixProfile, atmPrefixProfile_SpvcAddressPrefix_Address=atmPrefixProfile_SpvcAddressPrefix_Address, atmPrefixProfile_PnniNodePrefix_Address=atmPrefixProfile_PnniNodePrefix_Address, mibatmPrefixProfileEntry=mibatmPrefixProfileEntry, mibatmPrefixProfileTable=mibatmPrefixProfileTable, atmPrefixProfile_SvcAddressPrefix_Length=atmPrefixProfile_SvcAddressPrefix_Length, atmPrefixProfile_SpvcAddressPrefix_Length=atmPrefixProfile_SpvcAddressPrefix_Length, DisplayString=DisplayString, atmPrefixProfile_PnniNodePrefix_Length=atmPrefixProfile_PnniNodePrefix_Length, atmPrefixProfile_SvcAddressPrefix_Address=atmPrefixProfile_SvcAddressPrefix_Address, atmPrefixProfile_PrefixName=atmPrefixProfile_PrefixName, atmPrefixProfile_Action_o=atmPrefixProfile_Action_o, atmPrefixProfile_UseShortAddress=atmPrefixProfile_UseShortAddress)
