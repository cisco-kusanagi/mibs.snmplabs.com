#
# PySNMP MIB module ATM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATM-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:19:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, Bits, IpAddress, MibIdentifier, NotificationType, mib_2, Integer32, ObjectIdentity, Gauge32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "Bits", "IpAddress", "MibIdentifier", "NotificationType", "mib-2", "Integer32", "ObjectIdentity", "Gauge32", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
atmTCMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 37, 3))
if mibBuilder.loadTexts: atmTCMIB.setLastUpdated('9810190200Z')
if mibBuilder.loadTexts: atmTCMIB.setOrganization('IETF AToMMIB Working Group')
if mibBuilder.loadTexts: atmTCMIB.setContactInfo(' Michael Noto Postal: 3Com Corporation 5400 Bayfront Plaza, M/S 3109 Santa Clara, CA 95052 USA Tel: +1 408 326 2218 E-mail: mike_noto@3com.com Ethan Mickey Spiegel Postal: Cisco Systems 170 W. Tasman Dr. San Jose, CA 95134 USA Tel: +1 408 526 6408 E-mail: mspiegel@cisco.com Kaj Tesink Postal: Bellcore 331 Newman Springs Road Red Bank, NJ 07701 USA Tel: +1 732 758 5254 Fax: +1 732 758 4177 E-mail: kaj@bellcore.com')
if mibBuilder.loadTexts: atmTCMIB.setDescription('This MIB Module provides Textual Conventions and OBJECT-IDENTITY Objects to be used by ATM systems.')
class AtmAddr(TextualConvention, OctetString):
    description = 'An ATM address. The semantics are implied by the length. The address types are: - no address (0 octets) - E.164 (8 octets) - NSAP (20 octets) In addition, when subaddresses are used the AtmAddr may represent the concatenation of address and subaddress. The associated address types are: - E.164, E.164 (16 octets) - E.164, NSAP (28 octets) - NSAP, NSAP (40 octets) Address lengths other than defined in this definition imply address types defined elsewhere. Note: The E.164 address is encoded in BCD format.'
    status = 'current'
    displayHint = '1x'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 40)

class AtmConnCastType(TextualConvention, Integer32):
    description = 'The type of topology of a connection (point- to-point, point-to-multipoint). In the case of point-to-multipoint, the orientation of this VPL or VCL in the connection. On a host: - p2mpRoot indicates that the host is the root of the p2mp connection. - p2mpLeaf indicates that the host is a leaf of the p2mp connection. On a switch interface: - p2mpRoot indicates that cells received by the switching fabric from the interface are from the root of the p2mp connection. - p2mpLeaf indicates that cells transmitted to the interface from the switching fabric are to the leaf of the p2mp connection.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("p2p", 1), ("p2mpRoot", 2), ("p2mpLeaf", 3))

class AtmConnKind(TextualConvention, Integer32):
    description = 'The type of call control used for an ATM connection at a particular interface. The use is as follows: pvc(1) Virtual link of a PVC. Should not be used for an PVC/SVC (i.e., Soft PVC) crossconnect. svcIncoming(2) Virtual link established after a received signaling request to setup an SVC. svcOutgoing(3) Virtual link established after a transmitted or forwarded signaling request to setup an SVC. spvcInitiator(4) Virtual link at the PVC side of an SVC/PVC crossconnect, where the switch is the initiator of the Soft PVC setup. spvcTarget(5) Virtual link at the PVC side of an SVC/PVC crossconnect, where the switch is the target of the Soft PVC setup. For PVCs, a pvc virtual link is always cross- connected to a pvc virtual link. For SVCs, an svcIncoming virtual link is always cross- connected to an svcOutgoing virtual link. For Soft PVCs, an spvcInitiator is either cross-connected to an svcOutgoing or an spvcTarget, and an spvcTarget is either cross-connected to an svcIncoming or an spvcInitiator.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("pvc", 1), ("svcIncoming", 2), ("svcOutgoing", 3), ("spvcInitiator", 4), ("spvcTarget", 5))

class AtmIlmiNetworkPrefix(TextualConvention, OctetString):
    reference = 'ATM Forum, Integrated Local Management Interface (ILMI) Specification, Version 4.0, af-ilmi-0065.000, September 1996, Section 9 ATM Forum, ATM User-Network Interface Signalling Specification, Version 4.0 (UNI 4.0), af-sig-0061.000, June 1996, Section 3'
    description = 'A network prefix used for ILMI address registration. In the case of ATM endsystem addresses (AESAs), the network prefix is the first 13 octets of the address which includes the AFI, IDI, and HO-DSP fields. In the case of native E.164 addresses, the network prefix is the entire E.164 address encoded in 8 octets, as if it were an E.164 IDP in an ATM endsystem address structure.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(8, 8), ValueSizeConstraint(13, 13), )
class AtmInterfaceType(TextualConvention, Integer32):
    description = 'The connection setup procedures used for the identified interface. Other: Connection setup procedures other than those listed below. Auto-configuration: Indicates that the connection setup procedures are to be determined dynamically, or that determination has not yet been completed. One such mechanism is via ATM Forum ILMI auto-configuration procedures. ITU-T DSS2: - ITU-T Recommendation Q.2931, Broadband Integrated Service Digital Network (B-ISDN) Digital Subscriber Signalling System No.2 (DSS2) User-Network Interface (UNI) Layer 3 Specification for Basic Call/Connection Control (September 1994) - ITU-T Draft Recommendation Q.2961, B-ISDN DSS 2 Support of Additional Traffic Parameters (May 1995) - ITU-T Draft Recommendation Q.2971, B-ISDN DSS 2 User Network Interface Layer 3 Specification for Point-to-multipoint Call/connection Control (May 1995) ATM Forum UNI 3.0: ATM Forum, ATM User-Network Interface, Version 3.0 (UNI 3.0) Specification, (1994). ATM Forum UNI 3.1: ATM Forum, ATM User-Network Interface, Version 3.1 (UNI 3.1) Specification, (November 1994). ATM Forum UNI Signalling 4.0: ATM Forum, ATM User-Network Interface (UNI) Signalling Specification Version 4.0, af-sig-0061.000 (June 1996). ATM Forum IISP (based on UNI 3.0 or UNI 3.1) : Interim Inter-switch Signaling Protocol (IISP) Specification, Version 1.0, af-pnni-0026.000, (December 1994). ATM Forum PNNI 1.0 : ATM Forum, Private Network-Network Interface Specification, Version 1.0, af-pnni-0055.000, (March 1996). ATM Forum B-ICI: ATM Forum, B-ICI Specification, Version 2.0, af-bici-0013.002, (November 1995). ATM Forum UNI PVC Only: An ATM Forum compliant UNI with the signalling disabled. ATM Forum NNI PVC Only: An ATM Forum compliant NNI with the signalling disabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
    namedValues = NamedValues(("other", 1), ("autoConfig", 2), ("ituDss2", 3), ("atmfUni3Dot0", 4), ("atmfUni3Dot1", 5), ("atmfUni4Dot0", 6), ("atmfIispUni3Dot0", 7), ("atmfIispUni3Dot1", 8), ("atmfIispUni4Dot0", 9), ("atmfPnni1Dot0", 10), ("atmfBici2Dot0", 11), ("atmfUniPvcOnly", 12), ("atmfNniPvcOnly", 13))

class AtmServiceCategory(TextualConvention, Integer32):
    reference = 'ATM Forum Traffic Management Specification, Version 4.0, af-tm-0056.000, June 1996.'
    description = 'The service category for a connection.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("other", 1), ("cbr", 2), ("rtVbr", 3), ("nrtVbr", 4), ("abr", 5), ("ubr", 6))

class AtmSigDescrParamIndex(TextualConvention, Integer32):
    description = 'The value of this object identifies a row in the atmSigDescrParamTable. The value 0 signifies that none of the signalling parameters defined in the atmSigDescrParamTable are applicable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AtmTrafficDescrParamIndex(TextualConvention, Integer32):
    description = 'The value of this object identifies a row in the atmTrafficDescrParamTable. The value 0 signifies that no row has been identified.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 2147483647)

class AtmVcIdentifier(TextualConvention, Integer32):
    description = 'The VCI value for a VCL. The maximum VCI value cannot exceed the value allowable by atmInterfaceMaxVciBits defined in ATM-MIB.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class AtmVpIdentifier(TextualConvention, Integer32):
    description = 'The VPI value for a VPL or VCL. The value VPI=0 is only allowed for a VCL. For ATM UNIs supporting VPCs the VPI value ranges from 0 to 255. The VPI value 0 is supported for ATM UNIs conforming to the ATM Forum UNI 4.0 Annex 8 (Virtual UNIs) specification. For ATM UNIs supporting VCCs the VPI value ranges from 0 to 255. For ATM NNIs the VPI value ranges from 0 to 4095. The maximum VPI value cannot exceed the value allowable by atmInterfaceMaxVpiBits defined in ATM-MIB.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class AtmVorXAdminStatus(TextualConvention, Integer32):
    description = 'The value determines the desired administrative status of a virtual link or cross-connect. The up and down states indicate that the traffic flow is enabled or disabled respectively on the virtual link or cross-connect.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("up", 1), ("down", 2))

class AtmVorXLastChange(TextualConvention, TimeTicks):
    description = "The value of MIB II's sysUpTime at the time a virtual link or cross-connect entered its current operational state. If the current state was entered prior to the last re-initialization of the agent then this object contains a zero value."
    status = 'current'

class AtmVorXOperStatus(TextualConvention, Integer32):
    description = 'The value determines the operational status of a virtual link or cross-connect. The up and down states indicate that the traffic flow is enabled or disabled respectively on the virtual link or cross-connect. The unknown state indicates that the state of it cannot be determined. The state will be down or unknown if the supporting ATM interface(s) is down or unknown respectively.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("up", 1), ("down", 2), ("unknown", 3))

atmTrafficDescriptorTypes = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 1, 1))
atmObjectIdentities = MibIdentifier((1, 3, 6, 1, 2, 1, 37, 3, 1))
atmNoTrafficDescriptor = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 1))
if mibBuilder.loadTexts: atmNoTrafficDescriptor.setStatus('deprecated')
if mibBuilder.loadTexts: atmNoTrafficDescriptor.setDescription('This identifies the no ATM traffic descriptor type. Parameters 1, 2, 3, 4, and 5 are not used. This traffic descriptor type can be used for best effort traffic.')
atmNoClpNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 2))
if mibBuilder.loadTexts: atmNoClpNoScr.setStatus('current')
if mibBuilder.loadTexts: atmNoClpNoScr.setDescription('This traffic descriptor type is for no CLP and no Sustained Cell Rate. The use of the parameter vector for this type: Parameter 1: peak cell rate in cells/second for CLP=0+1 traffic Parameter 2: not used Parameter 3: not used Parameter 4: not used Parameter 5: not used.')
if mibBuilder.loadTexts: atmNoClpNoScr.setReference('ATM Forum,ATM User-Network Interface, Version 3.0 (UNI 3.0) Specification, 1994. ATM Forum, ATM User-Network Interface, Version 3.1 (UNI 3.1) Specification, November 1994.')
atmClpNoTaggingNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 3))
if mibBuilder.loadTexts: atmClpNoTaggingNoScr.setStatus('deprecated')
if mibBuilder.loadTexts: atmClpNoTaggingNoScr.setDescription('This traffic descriptor is for CLP without tagging and no Sustained Cell Rate. The use of the parameter vector for this type: Parameter 1: peak cell rate in cells/second for CLP=0+1 traffic Parameter 2: peak cell rate in cells/second for CLP=0 traffic Parameter 3: not used Parameter 4: not used Parameter 5: not used.')
atmClpTaggingNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 4))
if mibBuilder.loadTexts: atmClpTaggingNoScr.setStatus('deprecated')
if mibBuilder.loadTexts: atmClpTaggingNoScr.setDescription('This traffic descriptor is for CLP with tagging and no Sustained Cell Rate. The use of the parameter vector for this type: Parameter 1: peak cell rate in cells/second for CLP=0+1 traffic Parameter 2: peak cell rate in cells/second for CLP=0 traffic, excess tagged as CLP=1 Parameter 3: not used Parameter 4: not used Parameter 5: not used.')
atmNoClpScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 5))
if mibBuilder.loadTexts: atmNoClpScr.setStatus('current')
if mibBuilder.loadTexts: atmNoClpScr.setDescription('This traffic descriptor type is for no CLP with Sustained Cell Rate. The use of the parameter vector for this type: Parameter 1: peak cell rate in cells/second for CLP=0+1 traffic Parameter 2: sustainable cell rate in cells/second for CLP=0+1 traffic Parameter 3: maximum burst size in cells Parameter 4: not used Parameter 5: not used.')
if mibBuilder.loadTexts: atmNoClpScr.setReference('ATM Forum,ATM User-Network Interface, Version 3.0 (UNI 3.0) Specification, 1994. ATM Forum, ATM User-Network Interface, Version 3.1 (UNI 3.1) Specification, November 1994.')
atmClpNoTaggingScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 6))
if mibBuilder.loadTexts: atmClpNoTaggingScr.setStatus('current')
if mibBuilder.loadTexts: atmClpNoTaggingScr.setDescription('This traffic descriptor type is for CLP with Sustained Cell Rate and no tagging. The use of the parameter vector for this type: Parameter 1: peak cell rate in cells/second for CLP=0+1 traffic Parameter 2: sustainable cell rate in cells/second for CLP=0 traffic Parameter 3: maximum burst size in cells Parameter 4: not used Parameter 5: not used.')
if mibBuilder.loadTexts: atmClpNoTaggingScr.setReference('ATM Forum,ATM User-Network Interface, Version 3.0 (UNI 3.0) Specification, 1994. ATM Forum, ATM User-Network Interface, Version 3.1 (UNI 3.1) Specification, November 1994.')
atmClpTaggingScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 7))
if mibBuilder.loadTexts: atmClpTaggingScr.setStatus('current')
if mibBuilder.loadTexts: atmClpTaggingScr.setDescription('This traffic descriptor type is for CLP with tagging and Sustained Cell Rate. The use of the parameter vector for this type: Parameter 1: peak cell rate in cells/second for CLP=0+1 traffic Parameter 2: sustainable cell rate in cells/second for CLP=0 traffic, excess tagged as CLP=1 Parameter 3: maximum burst size in cells Parameter 4: not used Parameter 5: not used.')
if mibBuilder.loadTexts: atmClpTaggingScr.setReference('ATM Forum,ATM User-Network Interface, Version 3.0 (UNI 3.0) Specification, 1994. ATM Forum, ATM User-Network Interface, Version 3.1 (UNI 3.1) Specification, November 1994.')
atmClpNoTaggingMcr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 8))
if mibBuilder.loadTexts: atmClpNoTaggingMcr.setStatus('current')
if mibBuilder.loadTexts: atmClpNoTaggingMcr.setDescription('This traffic descriptor type is for CLP with Minimum Cell Rate and no tagging. The use of the parameter vector for this type: Parameter 1: peak cell rate in cells/second for CLP=0+1 traffic Parameter 2: CDVT in tenths of microseconds Parameter 3: minimum cell rate in cells/second Parameter 4: unused Parameter 5: unused.')
if mibBuilder.loadTexts: atmClpNoTaggingMcr.setReference('ATM Forum,ATM User-Network Interface, Version 3.0 (UNI 3.0) Specification, 1994. ATM Forum, ATM User-Network Interface, Version 3.1 (UNI 3.1) Specification, November 1994.')
atmClpTransparentNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 9))
if mibBuilder.loadTexts: atmClpTransparentNoScr.setStatus('current')
if mibBuilder.loadTexts: atmClpTransparentNoScr.setDescription('This traffic descriptor type is for the CLP- transparent model and no Sustained Cell Rate. The use of the parameter vector for this type: Parameter 1: peak cell rate in cells/second for CLP=0+1 traffic Parameter 2: CDVT in tenths of microseconds Parameter 3: not used Parameter 4: not used Parameter 5: not used. This traffic descriptor type is applicable to connections following the CBR.1 conformance definition. Connections specifying this traffic descriptor type will be rejected at UNI 3.0 or UNI 3.1 interfaces. For a similar traffic descriptor type that can be accepted at UNI 3.0 and UNI 3.1 interfaces, see atmNoClpNoScr.')
if mibBuilder.loadTexts: atmClpTransparentNoScr.setReference('ATM Forum,ATM User-Network Interface, Version 3.0 (UNI 3.0) Specification, 1994. ATM Forum, ATM User-Network Interface, Version 3.1 (UNI 3.1) Specification, November 1994. ATM Forum, Traffic Management Specification, Version 4.0, af-tm-0056.000, June 1996.')
atmClpTransparentScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 10))
if mibBuilder.loadTexts: atmClpTransparentScr.setStatus('current')
if mibBuilder.loadTexts: atmClpTransparentScr.setDescription('This traffic descriptor type is for the CLP- transparent model with Sustained Cell Rate. The use of the parameter vector for this type: Parameter 1: peak cell rate in cells/second for CLP=0+1 traffic Parameter 2: sustainable cell rate in cells/second for CLP=0+1 traffic Parameter 3: maximum burst size in cells Parameter 4: CDVT in tenths of microseconds Parameter 5: not used. This traffic descriptor type is applicable to connections following the VBR.1 conformance definition. Connections specifying this traffic descriptor type will be rejected at UNI 3.0 or UNI 3.1 interfaces. For a similar traffic descriptor type that can be accepted at UNI 3.0 and UNI 3.1 interfaces, see atmNoClpScr.')
if mibBuilder.loadTexts: atmClpTransparentScr.setReference('ATM Forum,ATM User-Network Interface, Version 3.0 (UNI 3.0) Specification, 1994. ATM Forum, ATM User-Network Interface, Version 3.1 (UNI 3.1) Specification, November 1994. ATM Forum, Traffic Management Specification, Version 4.0, af-tm-0056.000, June 1996.')
atmNoClpTaggingNoScr = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 11))
if mibBuilder.loadTexts: atmNoClpTaggingNoScr.setStatus('current')
if mibBuilder.loadTexts: atmNoClpTaggingNoScr.setDescription('This traffic descriptor type is for no CLP with tagging and no Sustained Cell Rate. The use of the parameter vector for this type: Parameter 1: peak cell rate in cells/second for CLP=0+1 traffic Parameter 2: CDVT in tenths of microseconds Parameter 3: not used Parameter 4: not used Parameter 5: not used. This traffic descriptor type is applicable to connections following the UBR.2 conformance definition .')
if mibBuilder.loadTexts: atmNoClpTaggingNoScr.setReference('ATM Forum,ATM User-Network Interface, Version 3.0 (UNI 3.0) Specification, 1994. ATM Forum, ATM User-Network Interface, Version 3.1 (UNI 3.1) Specification, November 1994. ATM Forum, Traffic Management Specification, Version 4.0, af-tm-0056.000, June 1996.')
atmNoClpNoScrCdvt = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 12))
if mibBuilder.loadTexts: atmNoClpNoScrCdvt.setStatus('current')
if mibBuilder.loadTexts: atmNoClpNoScrCdvt.setDescription('This traffic descriptor type is for no CLP and no Sustained Cell Rate. The use of the parameter vector for this type: Parameter 1: peak cell rate in cells/second for CLP=0+1 traffic Parameter 2: CDVT in tenths of microseconds Parameter 3: not used Parameter 4: not used Parameter 5: not used. This traffic descriptor type is applicable to CBR connections following the UNI 3.0/3.1 conformance definition for PCR CLP=0+1. These CBR connections differ from CBR.1 connections in that the CLR objective applies only to the CLP=0 cell flow. This traffic descriptor type is also applicable to connections following the UBR.1 conformance definition.')
if mibBuilder.loadTexts: atmNoClpNoScrCdvt.setReference('ATM Forum,ATM User-Network Interface, Version 3.0 (UNI 3.0) Specification, 1994. ATM Forum, ATM User-Network Interface, Version 3.1 (UNI 3.1) Specification, November 1994. ATM Forum, Traffic Management Specification, Version 4.0, af-tm-0056.000, June 1996.')
atmNoClpScrCdvt = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 13))
if mibBuilder.loadTexts: atmNoClpScrCdvt.setStatus('current')
if mibBuilder.loadTexts: atmNoClpScrCdvt.setDescription('This traffic descriptor type is for no CLP with Sustained Cell Rate. The use of the parameter vector for this type: Parameter 1: peak cell rate in cells/second for CLP=0+1 traffic Parameter 2: sustainable cell rate in cells/second for CLP=0+1 traffic Parameter 3: maximum burst size in cells Parameter 4: CDVT in tenths of microseconds Parameter 5: not used. This traffic descriptor type is applicable to VBR connections following the UNI 3.0/3.1 conformance definition for PCR CLP=0+1 and SCR CLP=0+1. These VBR connections differ from VBR.1 connections in that the CLR objective applies only to the CLP=0 cell flow.')
if mibBuilder.loadTexts: atmNoClpScrCdvt.setReference('ATM Forum,ATM User-Network Interface, Version 3.0 (UNI 3.0) Specification, 1994. ATM Forum, ATM User-Network Interface, Version 3.1 (UNI 3.1) Specification, November 1994. ATM Forum, Traffic Management Specification, Version 4.0, af-tm-0056.000, June 1996.')
atmClpNoTaggingScrCdvt = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 14))
if mibBuilder.loadTexts: atmClpNoTaggingScrCdvt.setStatus('current')
if mibBuilder.loadTexts: atmClpNoTaggingScrCdvt.setDescription('This traffic descriptor type is for CLP with Sustained Cell Rate and no tagging. The use of the parameter vector for this type: Parameter 1: peak cell rate in cells/second for CLP=0+1 traffic Parameter 2: sustainable cell rate in cells/second for CLP=0 traffic Parameter 3: maximum burst size in cells Parameter 4: CDVT in tenths of microseconds Parameter 5: not used. This traffic descriptor type is applicable to connections following the VBR.2 conformance definition.')
if mibBuilder.loadTexts: atmClpNoTaggingScrCdvt.setReference('ATM Forum,ATM User-Network Interface, Version 3.0 (UNI 3.0) Specification, 1994. ATM Forum, ATM User-Network Interface, Version 3.1 (UNI 3.1) Specification, November 1994. ATM Forum, Traffic Management Specification, Version 4.0, af-tm-0056.000, June 1996.')
atmClpTaggingScrCdvt = ObjectIdentity((1, 3, 6, 1, 2, 1, 37, 1, 1, 15))
if mibBuilder.loadTexts: atmClpTaggingScrCdvt.setStatus('current')
if mibBuilder.loadTexts: atmClpTaggingScrCdvt.setDescription('This traffic descriptor type is for CLP with tagging and Sustained Cell Rate. The use of the parameter vector for this type: Parameter 1: peak cell rate in cells/second for CLP=0+1 traffic Parameter 2: sustainable cell rate in cells/second for CLP=0 traffic, excess tagged as CLP=1 Parameter 3: maximum burst size in cells Parameter 4: CDVT in tenths of microseconds Parameter 5: not used. This traffic descriptor type is applicable to connections following the VBR.3 conformance definition.')
if mibBuilder.loadTexts: atmClpTaggingScrCdvt.setReference('ATM Forum,ATM User-Network Interface, Version 3.0 (UNI 3.0) Specification, 1994. ATM Forum, ATM User-Network Interface, Version 3.1 (UNI 3.1) Specification, November 1994. ATM Forum, Traffic Management Specification, Version 4.0, af-tm-0056.000, June 1996.')
mibBuilder.exportSymbols("ATM-TC-MIB", PYSNMP_MODULE_ID=atmTCMIB, atmNoClpScr=atmNoClpScr, atmClpTaggingNoScr=atmClpTaggingNoScr, atmTrafficDescriptorTypes=atmTrafficDescriptorTypes, atmClpNoTaggingScr=atmClpNoTaggingScr, atmClpNoTaggingScrCdvt=atmClpNoTaggingScrCdvt, AtmIlmiNetworkPrefix=AtmIlmiNetworkPrefix, AtmSigDescrParamIndex=AtmSigDescrParamIndex, AtmVorXLastChange=AtmVorXLastChange, atmClpTaggingScr=atmClpTaggingScr, AtmConnKind=AtmConnKind, atmClpTransparentNoScr=atmClpTransparentNoScr, AtmConnCastType=AtmConnCastType, atmObjectIdentities=atmObjectIdentities, atmNoClpTaggingNoScr=atmNoClpTaggingNoScr, atmNoClpNoScr=atmNoClpNoScr, atmClpTransparentScr=atmClpTransparentScr, atmNoClpScrCdvt=atmNoClpScrCdvt, atmTCMIB=atmTCMIB, atmClpTaggingScrCdvt=atmClpTaggingScrCdvt, atmNoClpNoScrCdvt=atmNoClpNoScrCdvt, AtmVpIdentifier=AtmVpIdentifier, atmNoTrafficDescriptor=atmNoTrafficDescriptor, AtmVorXAdminStatus=AtmVorXAdminStatus, AtmAddr=AtmAddr, AtmTrafficDescrParamIndex=AtmTrafficDescrParamIndex, atmClpNoTaggingNoScr=atmClpNoTaggingNoScr, atmClpNoTaggingMcr=atmClpNoTaggingMcr, AtmVcIdentifier=AtmVcIdentifier, AtmServiceCategory=AtmServiceCategory, AtmInterfaceType=AtmInterfaceType, AtmVorXOperStatus=AtmVorXOperStatus)
