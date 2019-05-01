#
# PySNMP MIB module ASCEND-MIBATMADDRALIAS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBATMADDRALIAS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:25 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Gauge32, iso, IpAddress, Counter32, Unsigned32, Bits, Integer32, TimeTicks, Counter64, ObjectIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Gauge32", "iso", "IpAddress", "Counter32", "Unsigned32", "Bits", "Integer32", "TimeTicks", "Counter64", "ObjectIdentity", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
class DisplayString(OctetString):
    pass

mibatmAddrAliasProfile = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 37))
mibatmAddrAliasProfileTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 37, 1), )
if mibBuilder.loadTexts: mibatmAddrAliasProfileTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibatmAddrAliasProfileTable.setDescription('A list of mibatmAddrAliasProfile profile entries.')
mibatmAddrAliasProfileEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1), ).setIndexNames((0, "ASCEND-MIBATMADDRALIAS-MIB", "atmAddrAliasProfile-AliasName"))
if mibBuilder.loadTexts: mibatmAddrAliasProfileEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibatmAddrAliasProfileEntry.setDescription('A mibatmAddrAliasProfile entry containing objects that maps to the parameters of mibatmAddrAliasProfile profile.')
atmAddrAliasProfile_AliasName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1, 1), DisplayString()).setLabel("atmAddrAliasProfile-AliasName").setMaxAccess("readonly")
if mibBuilder.loadTexts: atmAddrAliasProfile_AliasName.setStatus('mandatory')
if mibBuilder.loadTexts: atmAddrAliasProfile_AliasName.setDescription('The alias name for the address.')
atmAddrAliasProfile_Address = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1, 2), DisplayString()).setLabel("atmAddrAliasProfile-Address").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmAddrAliasProfile_Address.setStatus('mandatory')
if mibBuilder.loadTexts: atmAddrAliasProfile_Address.setDescription('The address to be aliased.')
atmAddrAliasProfile_Length = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1, 3), Integer32()).setLabel("atmAddrAliasProfile-Length").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmAddrAliasProfile_Length.setStatus('mandatory')
if mibBuilder.loadTexts: atmAddrAliasProfile_Length.setDescription('The length of the address to be aliased in bytes.')
atmAddrAliasProfile_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 37, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("atmAddrAliasProfile-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: atmAddrAliasProfile_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: atmAddrAliasProfile_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBATMADDRALIAS-MIB", atmAddrAliasProfile_Length=atmAddrAliasProfile_Length, atmAddrAliasProfile_Address=atmAddrAliasProfile_Address, mibatmAddrAliasProfileEntry=mibatmAddrAliasProfileEntry, mibatmAddrAliasProfileTable=mibatmAddrAliasProfileTable, atmAddrAliasProfile_Action_o=atmAddrAliasProfile_Action_o, atmAddrAliasProfile_AliasName=atmAddrAliasProfile_AliasName, mibatmAddrAliasProfile=mibatmAddrAliasProfile, DisplayString=DisplayString)
