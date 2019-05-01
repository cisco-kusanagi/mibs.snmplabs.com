#
# PySNMP MIB module CISCO-IETF-PW-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-PW-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:51:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, Counter32, MibIdentifier, TimeTicks, ModuleIdentity, Integer32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Bits, ObjectIdentity, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Counter32", "MibIdentifier", "TimeTicks", "ModuleIdentity", "Integer32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Bits", "ObjectIdentity", "Unsigned32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cpwTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 20000, 1))
cpwTCMIB.setRevisions(('2006-07-21 12:00', '2003-02-26 12:00', '2002-05-28 12:00', '2002-01-30 12:00', '2001-12-20 12:00', '2001-07-12 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cpwTCMIB.setRevisionsDescriptions(('Added following enumerations to cpwVcType TC: e1Satop(12), t1Satop(13), e3Satop(14), t3Satop(15), basicCesPsn(16), basicTdmIp(17), tdmCasCesPsn(18), tdmCasTdmIp(19). The above enumerations are based on IANAPwTypeTC TC in draft-ietf-pwe3-pw-mib-08.txt', 'Made Cisco proprietary based on the PW-TC-MIB.my file extracted from draft-ietf-pwe3-pw-tc-mib-00.txt ', 'Adding PwVcType, and enhance some descriptions.', 'Adding PwVcVlanCfg, PwAddressType and PwOperStatus.', 'Remove PwVcInstance', 'Initial version.',))
if mibBuilder.loadTexts: cpwTCMIB.setLastUpdated('200607211200Z')
if mibBuilder.loadTexts: cpwTCMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: cpwTCMIB.setContactInfo(' Thomas D. Nadeau Postal: Cisco Systems, Inc. 250 Apollo Drive Chelmsford, MA 01824 Tel: +1-978-497-3051 Email: tnadeau@cisco.com MPLS MIB Development Team Postal: Cisco Systems, Inc. 250 Apollo Drive Chelmsford, MA 01924 Tel: +1-978-497-3989 Email: ch-mpls-mib-dev@cisco.com ')
if mibBuilder.loadTexts: cpwTCMIB.setDescription('This MIB Module provides Textual Conventions and OBJECT-IDENTITY Objects to be used PW services.')
cpwMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 10, 20000))
class CpwGroupID(TextualConvention, Unsigned32):
    description = 'An administrative identification mechanism for grouping a set of service-specific pseudo-wire services. May only have local significance.'
    status = 'current'

class CpwVcIDType(TextualConvention, Unsigned32):
    description = 'Virtual Circuit Identifier. Used to identify the VC (together with some other fields) in the signaling session. Zero if the VC is set-up manually.'
    status = 'current'

class CpwVcIndexType(TextualConvention, Unsigned32):
    description = 'Virtual Circuit Index. Locally unique index for indexing several MIB tables associated with a particular VC.'
    status = 'current'

class CpwVcVlanCfg(TextualConvention, Integer32):
    description = 'VLAN configuration for Ethernet PW. Values between 0 to 4095 indicate the actual VLAN field value. A value of 4096 indicates that the object refer to untagged frames, i.e. frames without 802.1Q field. A value of 4097 indicates that the object is not relevant.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4097)

class CpwOperStatus(TextualConvention, Integer32):
    description = "Indicate the operational status of the PW VC. - up: Ready to pass packets. - down: If PW signaling has not yet finished, or indications available at the service level indicate that the VC is not passing packets. - testing: If AdminStatus at the VC level is set to test. - dormant: The VC is not available because of the required resources are occupied VC with higher priority VCs . - notPresent: Some component is missing to accomplish the set up of the VC. - lowerLayerDown: The underlying PSN or outer tunnel is not in OperStatus 'up'. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7))

class CpwVcType(TextualConvention, Integer32):
    description = 'Indicate the VC type (i.e. the carried service). Note: the exact set of VC types is yet to be worked out by the WG. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("other", 0), ("frameRelay", 1), ("atmAal5Vcc", 2), ("atmTransparent", 3), ("ethernetVLAN", 4), ("ethernet", 5), ("hdlc", 6), ("ppp", 7), ("cep", 8), ("atmVccCell", 9), ("atmVpcCell", 10), ("ethernetVPLS", 11), ("e1Satop", 12), ("t1Satop", 13), ("e3Satop", 14), ("t3Satop", 15), ("basicCesPsn", 16), ("basicTdmIp", 17), ("tdmCasCesPsn", 18), ("tdmCasTdmIp", 19))

mibBuilder.exportSymbols("CISCO-IETF-PW-TC-MIB", CpwVcVlanCfg=CpwVcVlanCfg, CpwVcIDType=CpwVcIDType, CpwGroupID=CpwGroupID, CpwVcIndexType=CpwVcIndexType, cpwTCMIB=cpwTCMIB, CpwVcType=CpwVcType, CpwOperStatus=CpwOperStatus, PYSNMP_MODULE_ID=cpwTCMIB, cpwMIB=cpwMIB)
