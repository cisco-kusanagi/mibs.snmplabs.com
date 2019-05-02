#
# PySNMP MIB module PW-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PW-TC-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:45:18 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, ModuleIdentity, Unsigned32, Integer32, Counter32, mib_2, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ObjectIdentity, IpAddress, Bits, MibIdentifier, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ModuleIdentity", "Unsigned32", "Integer32", "Counter32", "mib-2", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ObjectIdentity", "IpAddress", "Bits", "MibIdentifier", "iso", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pwTcStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 188))
pwTcStdMIB.setRevisions(('2009-04-21 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: pwTcStdMIB.setRevisionsDescriptions(('Original Version',))
if mibBuilder.loadTexts: pwTcStdMIB.setLastUpdated('200904210000Z')
if mibBuilder.loadTexts: pwTcStdMIB.setOrganization('Pseudowire Edge-to-Edge Emulation (PWE3) Working Group')
if mibBuilder.loadTexts: pwTcStdMIB.setContactInfo(' Thomas D. Nadeau Email: tom.nadeau@bt.com David Zelig Email: davidz@oversi.com Orly Nicklass Email: orlyn@radvision.com The PWE3 Working Group (email distribution pwe3@ietf.org, http://www.ietf.org/html.charters/pwe3-charter.html) ')
if mibBuilder.loadTexts: pwTcStdMIB.setDescription("This MIB module defines TEXTUAL-CONVENTIONS for concepts used in pseudowire edge-to-edge networks. Copyright (c) 2009 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met: - Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer. - Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution. - Neither the name of Internet Society, IETF or IETF Trust, nor the names of specific contributors, may be used to endorse or promote products derived from this software without specific prior written permission. THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS' AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE. This version of this MIB module is part of RFC 5542; see the RFC itself for full legal notices.")
class PwGroupID(TextualConvention, Unsigned32):
    description = 'An administrative identification for grouping a set of service-specific pseudowire services.'
    status = 'current'
    displayHint = 'd'

class PwIDType(TextualConvention, Unsigned32):
    description = 'Pseudowire Identifier. Used to identify the PW (together with some other fields) in the signaling session.'
    status = 'current'
    displayHint = 'd'

class PwIndexType(TextualConvention, Unsigned32):
    description = 'Pseudowire Index. A unique value, greater than zero, for each locally defined PW. Used for indexing several MIB tables associated with the particular PW. It is recommended that values are assigned contiguously starting from 1. The value for each PW MUST remain constant at least from one re-initialization to the next re-initialization.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class PwIndexOrZeroType(TextualConvention, Unsigned32):
    description = 'This TEXTUAL-CONVENTION is an extension of the PwIndexType convention. The latter defines a greater- than-zero value used to identify a pseudowire in the managed system. This extension permits the additional value of zero. The zero value is object-specific and MUST therefore be defined as part of the description of any object that uses this syntax. Examples of the usage of zero might include situations where pseudowire was unknown, or where none or all pseudowires need to be referenced.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class PwOperStatusTC(TextualConvention, Integer32):
    description = "Indicates the operational status of the PW. - up(1): Ready to pass packets. - down(2): PW signaling is not yet finished, or indications available at the service level indicate that the PW is not passing packets. - testing(3): AdminStatus at the PW level is set to test. - dormant(4): The PW is not in a condition to pass packets but is in a 'pending' state, waiting for some external event. - notPresent(5): Some component is missing to accomplish the setup of the PW. It can be configuration error, incomplete configuration, or a missing H/W component. - lowerLayerDown(6): One or more of the lower-layer interfaces responsible for running the underlying PSN is not in OperStatus 'up' state."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("up", 1), ("down", 2), ("testing", 3), ("dormant", 4), ("notPresent", 5), ("lowerLayerDown", 6))

class PwAttachmentIdentifierType(TextualConvention, OctetString):
    description = 'An octet string used in the generalized Forward Error Correction (FEC) element for identifying attachment forwarder and groups. A NULL identifier is of zero length. '
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class PwGenIdType(TextualConvention, Unsigned32):
    description = 'Represents the Attachment Group Identifier (AGI) Type and Attachment Individual Identifier (AII) Type in generalized FEC signaling and configuration. '
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 254)

class PwCwStatusTC(TextualConvention, Integer32):
    reference = "Martini, et al., 'Pseudowire Setup and Maintenance Using the Label Distribution Protocol', [RFC4447]."
    description = 'Indicates the status of the control word (CW) negotiation based on the local configuration and the indications received from the peer node. waitingForNextMsg(1) indicates that the node is waiting for another label mapping from the peer. sentWrongBitErrorCode(2) indicates that the local node has notified the peer about a mismatch in the C-bit. rxWithdrawWithWrongBitErrorCode(3) indicates that a withdraw message has been received with the wrong C-bit error code. illegalReceivedBit(4) indicates a C-bit configuration with the peer that is not compatible with the PW type. cwPresent(5) indicates that the CW is present for this PW. If signaling is used, the C-bit is set and agreed upon between the nodes. For manually configured PW, the local configuration requires the use of the CW. cwNotPresent(6) indicates that the CW is not present for this PW. If signaling is used, the C-bit is reset and agreed upon between the nodes. For manually configured PW, the local configuration requires that the CW not be used. notYetKnown(7) indicates that a label mapping has not yet been received from the peer. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("waitingForNextMsg", 1), ("sentWrongBitErrorCode", 2), ("rxWithdrawWithWrongBitErrorCode", 3), ("illegalReceivedBit", 4), ("cwPresent", 5), ("cwNotPresent", 6), ("notYetKnown", 7))

class PwStatus(TextualConvention, Bits):
    description = 'Indicates the status of the PW and the interfaces affecting this PW. If none of the bits are set, it indicates no faults are reported. '
    status = 'current'
    namedValues = NamedValues(("pwNotForwarding", 0), ("servicePwRxFault", 1), ("servicePwTxFault", 2), ("psnPwRxFault", 3), ("psnPwTxFault", 4))

class PwFragSize(TextualConvention, Unsigned32):
    description = 'If set to a value other than zero, it indicates the desired fragmentation length in bytes. If set to zero, fragmentation is not desired for PSN bound packets. '
    status = 'current'
    displayHint = 'd'

class PwFragStatus(TextualConvention, Bits):
    reference = "Malis, A. and M. Townsley, 'Pseudowire Emulation Edge-to- Edge (PWE3) Fragmentation and Reassembly', [RFC4623]."
    description = 'Indicates the status of the fragmentation/reassembly process based on local configuration and peer capability. noFrag(0) bit indicates that local configuration is for no fragmentation. cfgFragGreaterThanPsnMtu(1) bit indicates that the local node is set to fragment, but the fragmentation size is greater than the MTU available at the PSN between the nodes. Fragmentation is not done in this case. cfgFragButRemoteIncapable(2) bit indicates that the local configuration conveys the desire for fragmentation but the peer is not capable of reassembly. remoteFragCapable(3) bit indicates that the remote node is capable to accept fragmented PDUs. fragEnabled(4) bit indicates that fragmentation will be used on this PW. Fragmentation can be used if the local node was configured for fragmentation, the peer has the capability to accept fragmented packets, and the CW is in use for this PW.'
    status = 'current'
    namedValues = NamedValues(("noFrag", 0), ("cfgFragGreaterThanPsnMtu", 1), ("cfgFragButRemoteIncapable", 2), ("remoteFragCapable", 3), ("fragEnabled", 4))

class PwCfgIndexOrzero(TextualConvention, Unsigned32):
    description = 'Index in any of the relevant configuration tables for supplement information regarding configuration of the specific technology. Value zero implies no additional configuration information is applicable.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

mibBuilder.exportSymbols("PW-TC-STD-MIB", PwAttachmentIdentifierType=PwAttachmentIdentifierType, PYSNMP_MODULE_ID=pwTcStdMIB, PwCwStatusTC=PwCwStatusTC, PwStatus=PwStatus, PwFragSize=PwFragSize, PwGenIdType=PwGenIdType, PwOperStatusTC=PwOperStatusTC, PwIDType=PwIDType, PwIndexType=PwIndexType, PwCfgIndexOrzero=PwCfgIndexOrzero, PwGroupID=PwGroupID, pwTcStdMIB=pwTcStdMIB, PwIndexOrZeroType=PwIndexOrZeroType, PwFragStatus=PwFragStatus)
