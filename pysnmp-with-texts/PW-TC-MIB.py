#
# PySNMP MIB module PW-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PW-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:42:55 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, MibIdentifier, Counter32, ModuleIdentity, Unsigned32, IpAddress, Gauge32, Counter64, experimental, Bits, iso, ObjectIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "MibIdentifier", "Counter32", "ModuleIdentity", "Unsigned32", "IpAddress", "Gauge32", "Counter64", "experimental", "Bits", "iso", "ObjectIdentity", "TimeTicks")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
pwTCMIB = ModuleIdentity((1, 3, 6, 1, 3, 8888, 1))
pwTCMIB.setRevisions(('2003-07-28 12:00', '2003-05-01 12:00', '1902-05-28 12:00', '1902-01-30 12:00', '2001-12-20 12:00', '2001-07-12 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pwTCMIB.setRevisionsDescriptions(('Adding objects to cover new control draft. Adapt VC types for current values in WG documents.', 'Adding PwVcAttachmentIdentifierType, Adapt VC types for current values in WG documents.', 'Adding PwVcType, and enhance some descriptions.', 'Adding PwVcVlanCfg, PwAddressType and PwOperStatus.', 'Remove PwVcInstance', 'Initial version.',))
if mibBuilder.loadTexts: pwTCMIB.setLastUpdated('200307281200Z')
if mibBuilder.loadTexts: pwTCMIB.setOrganization('Pseudo Wire Edge to Edge Emulation (PWE3) Working Group')
if mibBuilder.loadTexts: pwTCMIB.setContactInfo(' Thomas D. Nadeau Postal: Cisco Systems, Inc. 250 Apollo Drive Chelmsford, MA 01824 Tel: +1-978-497-3051 Email: tnadeau@cisco.com Dave Danenberg Postal: Litchfield Communications, Inc. 76 Westbury Park Rd Princeton Building East Watertown, CT 06795 Tel: +1-860-945-1573 x3180 Email: dave_danenberg@litchfieldcomm.com David Zelig Postal: Corrigent Systems. 126, Yigal Alon St. Tel Aviv, ISRAEL Phone: +972-3-6945273 E-mail: davidz@corrigent.com Andrew G. Malis Postal: Tellabs, Inc. 2730 Orchard Parkway San Jose, CA 95134 Email: Andy.Malis@tellabs.com PWE3 Working Group Mailing List: pwe3@ietf.org')
if mibBuilder.loadTexts: pwTCMIB.setDescription('This MIB Module provides Textual Conventions and OBJECT-IDENTITY Objects to be used PW services.')
pwMIB = MibIdentifier((1, 3, 6, 1, 3, 8888))
class PwGroupID(TextualConvention, Unsigned32):
    description = 'An administrative identification mechanism for grouping a set of service-specific pseudo-wire services. May only have local significance.'
    status = 'current'

class PwVcIDType(TextualConvention, Unsigned32):
    description = 'Virtual Circuit Identifier. Used to identify the VC (together with some other fields) in the signaling session. Zero if the VC is set-up manually.'
    status = 'current'

class PwVcIndexType(TextualConvention, Unsigned32):
    description = 'Virtual Circuit Index. Locally unique index for indexing several MIB tables associated with a particular VC.'
    status = 'current'

class PwVcVlanCfg(TextualConvention, Integer32):
    description = 'VLAN configuration for Ethernet PW. Values between 0 to 4095 indicate the actual VLAN field value. A value of 4096 indicates that the object refer to untagged frames, i.e. frames without 802.1Q field. A value of 4097 indicates that the object is not relevant.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4097)

class PwOperStatus(TextualConvention, Integer32):
    description = "Indicate the operational status of the PW VC. - up: Ready to pass packets. - down: If PW signaling has not yet finished, or indications available at the service level indicate that the VC is not passing packets. - testing: If AdminStatus at the PW level is set to test. - dormant: The PW is not available because of the required resources are occupied PW with higher priority PWs . - notPresent: Some component is missing to accomplish the set up of the PW. - lowerLayerDown: The underlying PSN or outer tunnel is not in OperStatus 'up'. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("unknown", 4), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7))

class PwVcType(TextualConvention, Integer32):
    description = 'Indicate the VC type (i.e. the carried service). Note: the exact set of VC types is yet to be worked out by the WG. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("other", 0), ("frameRelayDlci", 1), ("atmAal5SduVcc", 2), ("atmTransparent", 3), ("ethernetTagged", 4), ("ethernet", 5), ("hdlc", 6), ("ppp", 7), ("cem", 8), ("atmCellNto1Vcc", 9), ("atmCellNto1Vpc", 10), ("ipLayer2Transport", 11), ("atmCell1to1Vcc", 12), ("atmCell1to1Vpc", 13), ("atmAal5PduVcc", 14), ("frameRelayPortMode", 15), ("cep", 16))

class PwVcAttachmentIdentifierType(TextualConvention, OctetString):
    description = 'An octet string used in the generalized FEC element for identifying attachment forwarder and groups. The NULL identifier is of zero length. '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class PwVcCw(TruthValue):
    description = 'If true, indicate the existence or configuration of control word. '
    status = 'current'

class PwVcRemoteCwStatus(TextualConvention, Integer32):
    description = 'Indicate the status of the control word as advertized by the remote. notApplicable is set by the agent for manulaly configured PW. waitingForNextMsg indicate that the node is waiting for another label mapping from the remote. sentWrongBitErrorCode indicate that the local node has notified the peer about mismatch in the C bit. rxWithdrawWithWrongBitErrorCode indicate that a withdraw message has been recieved with wrong C-bit error code. illegalRecievedBit indicate a C bit configuration with the remote which is not compatible with the PW type. sameAsSent indicate consistent C bit setting between the peers. notYetKnown indicate that a label mapping has not yet recieved from the peer. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("notApplicable", 0), ("waitingForNextMsg", 1), ("sentWrongBitErrorCode", 2), ("rxWithdrawWithWrongBitErrorCode", 3), ("illegalRecievedBit", 4), ("sameAsSent", 5), ("notYetKnown", 6))

class PwVcCapabilities(TextualConvention, Bits):
    description = 'Indicate the optional capabilities of the control protocol. A value of zero indicate the basic LDP PW signaling. Values may be added in the future based on new capabilities introduced in IETF documents. '
    status = 'current'
    namedValues = NamedValues(("pwStatusIndication", 0))

class PwVcStatus(TextualConvention, Bits):
    description = 'The status of the PW and the interfaces affecting this PW. '
    status = 'current'
    namedValues = NamedValues(("pwNotForwarding", 0), ("customerFacingPwRxFault", 1), ("customerFacingPwTxFault", 2), ("psnFacingPwRxFault", 3), ("psnFacingPwTxFault", 4))

class PwVcFragSize(TextualConvention, Unsigned32):
    description = 'If set to value other than zero, it indicates desired fragmantation to the value set. If set to zero, fragmantation is not desired for PSN bound packets. '
    status = 'current'

class PwVcFragStatus(TextualConvention, Bits):
    description = "The status of the fragmantation process based on local configuration and the remote capability. noFragmantation bit indicate that local configuration is for no fragmantation. cfgFragGreaterThanPsnMtu bit indicate the local desire to fragment, but the fragamentation size desired is greater than the MTU available at the PSN between peers. Fragmantation is not done in this case. cfgFragButRemoteIncapable bit indicate local configuration indicate the desire for fragmantation but the remote is not capable of fragmantation. remoteFragCapable bit indicate that the remote has advertized it's fragmantation capability. fragmantationEnabled bit indicate that both the local was configured for fragmantation and the remote has the cabability to accept fragmented packets. "
    status = 'current'
    namedValues = NamedValues(("noFragmantation", 0), ("cfgFragGreaterThanPsnMtu", 1), ("cfgFragButRemoteIncapable", 2), ("remoteFragCapable", 3), ("fragmantationEnabled", 4))

mibBuilder.exportSymbols("PW-TC-MIB", PwVcCw=PwVcCw, pwMIB=pwMIB, PwVcVlanCfg=PwVcVlanCfg, PwGroupID=PwGroupID, PwOperStatus=PwOperStatus, PwVcCapabilities=PwVcCapabilities, PwVcType=PwVcType, PwVcIDType=PwVcIDType, PwVcFragStatus=PwVcFragStatus, PwVcFragSize=PwVcFragSize, PYSNMP_MODULE_ID=pwTCMIB, pwTCMIB=pwTCMIB, PwVcAttachmentIdentifierType=PwVcAttachmentIdentifierType, PwVcStatus=PwVcStatus, PwVcRemoteCwStatus=PwVcRemoteCwStatus, PwVcIndexType=PwVcIndexType)
