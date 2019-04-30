#
# PySNMP MIB module ATM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATM-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:04:02 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, NotificationType, Integer32, ModuleIdentity, TimeTicks, Gauge32, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, iso, MibIdentifier, IpAddress, Counter32, Unsigned32, mib_2 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "Integer32", "ModuleIdentity", "TimeTicks", "Gauge32", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "iso", "MibIdentifier", "IpAddress", "Counter32", "Unsigned32", "mib-2")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 37, 3))
if mibBuilder.loadTexts: atmTCMIB.setLastUpdated('9810190200Z')
if mibBuilder.loadTexts: atmTCMIB.setOrganization('IETF AToMMIB Working Group')
class AtmAddr(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 40)

class AtmConnCastType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("p2p", 1), ("p2mpRoot", 2), ("p2mpLeaf", 3))

class AtmConnKind(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("pvc", 1), ("svcIncoming", 2), ("svcOutgoing", 3), ("spvcInitiator", 4), ("spvcTarget", 5))

class AtmIlmiNetworkPrefix(TextualConvention, OctetString):
    reference = 'ATM Forum, Integrated Local Management Interface (ILMI) Specification, Version 4.0, af-ilmi-0065.000, September 1996, Section 9 ATM Forum, ATM User-Network Interface Signalling Specification, Version 4.0 (UNI 4.0), af-sig-0061.000, June 1996, Section 3'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(13, 13), )
class AtmInterfaceType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("other", 1), ("autoConfig", 2), ("ituDss2", 3), ("atmfUni3Dot0", 4), ("atmfUni3Dot1", 5), ("atmfUni4Dot0", 6), ("atmfIispUni3Dot0", 7), ("atmfIispUni3Dot1", 8), ("atmfIispUni4Dot0", 9), ("atmfPnni1Dot0", 10), ("atmfBici2Dot0", 11), ("atmfUniPvcOnly", 12), ("atmfNniPvcOnly", 13))

class AtmServiceCategory(TextualConvention, Integer32):
    reference = 'ATM Forum Traffic Management Specification, Version 4.0, af-tm-0056.000, June 1996.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("cbr", 2), ("rtVbr", 3), ("nrtVbr", 4), ("abr", 5), ("ubr", 6))

class AtmSigDescrParamIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AtmTrafficDescrParamIndex(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AtmVcIdentifier(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AtmVpIdentifier(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class AtmVorXAdminStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class AtmVorXLastChange(TextualConvention, TimeTicks):
    status = 'current'

class AtmVorXOperStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("unknown", 3))

atmTrafficDescriptorTypes = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1))
atmObjectIdentities = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 3, 1))
atmNoTrafficDescriptor = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 1))
if mibBuilder.loadTexts: atmNoTrafficDescriptor.setStatus('deprecated')
atmNoClpNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 2))
if mibBuilder.loadTexts: atmNoClpNoScr.setStatus('current')
atmClpNoTaggingNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 3))
if mibBuilder.loadTexts: atmClpNoTaggingNoScr.setStatus('deprecated')
atmClpTaggingNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 4))
if mibBuilder.loadTexts: atmClpTaggingNoScr.setStatus('deprecated')
atmNoClpScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 5))
if mibBuilder.loadTexts: atmNoClpScr.setStatus('current')
atmClpNoTaggingScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 6))
if mibBuilder.loadTexts: atmClpNoTaggingScr.setStatus('current')
atmClpTaggingScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 7))
if mibBuilder.loadTexts: atmClpTaggingScr.setStatus('current')
atmClpNoTaggingMcr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 8))
if mibBuilder.loadTexts: atmClpNoTaggingMcr.setStatus('current')
atmClpTransparentNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 9))
if mibBuilder.loadTexts: atmClpTransparentNoScr.setStatus('current')
atmClpTransparentScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 10))
if mibBuilder.loadTexts: atmClpTransparentScr.setStatus('current')
atmNoClpTaggingNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 11))
if mibBuilder.loadTexts: atmNoClpTaggingNoScr.setStatus('current')
atmNoClpNoScrCdvt = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 12))
if mibBuilder.loadTexts: atmNoClpNoScrCdvt.setStatus('current')
atmNoClpScrCdvt = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 13))
if mibBuilder.loadTexts: atmNoClpScrCdvt.setStatus('current')
atmClpNoTaggingScrCdvt = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 14))
if mibBuilder.loadTexts: atmClpNoTaggingScrCdvt.setStatus('current')
atmClpTaggingScrCdvt = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 15))
if mibBuilder.loadTexts: atmClpTaggingScrCdvt.setStatus('current')
mibBuilder.exportSymbols("ATM-TC-MIB", atmNoTrafficDescriptor=atmNoTrafficDescriptor, PYSNMP_MODULE_ID=atmTCMIB, AtmInterfaceType=AtmInterfaceType, AtmVcIdentifier=AtmVcIdentifier, atmClpTaggingScr=atmClpTaggingScr, AtmVpIdentifier=AtmVpIdentifier, atmObjectIdentities=atmObjectIdentities, atmNoClpNoScrCdvt=atmNoClpNoScrCdvt, AtmIlmiNetworkPrefix=AtmIlmiNetworkPrefix, atmClpNoTaggingMcr=atmClpNoTaggingMcr, AtmServiceCategory=AtmServiceCategory, atmNoClpScrCdvt=atmNoClpScrCdvt, AtmVorXAdminStatus=AtmVorXAdminStatus, AtmVorXLastChange=AtmVorXLastChange, AtmSigDescrParamIndex=AtmSigDescrParamIndex, AtmAddr=AtmAddr, atmNoClpScr=atmNoClpScr, atmTrafficDescriptorTypes=atmTrafficDescriptorTypes, AtmVorXOperStatus=AtmVorXOperStatus, atmClpTaggingScrCdvt=atmClpTaggingScrCdvt, AtmTrafficDescrParamIndex=AtmTrafficDescrParamIndex, AtmConnKind=AtmConnKind, atmClpTaggingNoScr=atmClpTaggingNoScr, AtmConnCastType=AtmConnCastType, atmClpNoTaggingScr=atmClpNoTaggingScr, atmNoClpTaggingNoScr=atmNoClpTaggingNoScr, atmClpNoTaggingScrCdvt=atmClpNoTaggingScrCdvt, atmNoClpNoScr=atmNoClpNoScr, atmClpNoTaggingNoScr=atmClpNoTaggingNoScr, atmTCMIB=atmTCMIB, atmClpTransparentScr=atmClpTransparentScr, atmClpTransparentNoScr=atmClpTransparentNoScr)
