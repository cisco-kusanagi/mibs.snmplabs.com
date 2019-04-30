#
# PySNMP MIB module ASCEND-MIBATMADDRALIAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBATMADDRALIAS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:10:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, iso, Counter32, Counter64, NotificationType, Gauge32, ObjectIdentity, Bits, TimeTicks, Unsigned32, ModuleIdentity, IpAddress, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "iso", "Counter32", "Counter64", "NotificationType", "Gauge32", "ObjectIdentity", "Bits", "TimeTicks", "Unsigned32", "ModuleIdentity", "IpAddress", "Integer32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibatmAddrAliasProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 37))
mibatmAddrAliasProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 37, 1), )
if mibBuilder.loadTexts: mibatmAddrAliasProfileTable.setStatus('mandatory')
mibatmAddrAliasProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1), ).setIndexNames((0, "ASCEND-MIBATMADDRALIAS-MIB", "atmAddrAliasProfile-AliasName"))
if mibBuilder.loadTexts: mibatmAddrAliasProfileEntry.setStatus('mandatory')
atmAddrAliasProfile_AliasName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1, 1), DisplayString()).setLabel("atmAddrAliasProfile-AliasName").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmAddrAliasProfile_AliasName.setStatus('mandatory')
atmAddrAliasProfile_Address = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1, 2), DisplayString()).setLabel("atmAddrAliasProfile-Address").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmAddrAliasProfile_Address.setStatus('mandatory')
atmAddrAliasProfile_Length = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1, 3), Integer32()).setLabel("atmAddrAliasProfile-Length").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmAddrAliasProfile_Length.setStatus('mandatory')
atmAddrAliasProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("atmAddrAliasProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmAddrAliasProfile_Action_o.setStatus('mandatory')
mibBuilder.exportSymbols("ASCEND-MIBATMADDRALIAS-MIB", mibatmAddrAliasProfileTable=mibatmAddrAliasProfileTable, mibatmAddrAliasProfileEntry=mibatmAddrAliasProfileEntry, atmAddrAliasProfile_Length=atmAddrAliasProfile_Length, atmAddrAliasProfile_Address=atmAddrAliasProfile_Address, DisplayString=DisplayString, mibatmAddrAliasProfile=mibatmAddrAliasProfile, atmAddrAliasProfile_Action_o=atmAddrAliasProfile_Action_o, atmAddrAliasProfile_AliasName=atmAddrAliasProfile_AliasName)
