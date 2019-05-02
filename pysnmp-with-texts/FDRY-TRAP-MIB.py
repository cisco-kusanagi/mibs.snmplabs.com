#
# PySNMP MIB module FDRY-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FDRY-TRAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:13:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
fdryTrap, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "fdryTrap")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, IpAddress, MibIdentifier, Bits, Gauge32, Unsigned32, Integer32, Counter32, iso, Counter64, TimeTicks, ObjectIdentity, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "IpAddress", "MibIdentifier", "Bits", "Gauge32", "Unsigned32", "Integer32", "Counter32", "iso", "Counter64", "TimeTicks", "ObjectIdentity", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
fdryTrapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1))
fdryTrapMIB.setRevisions(('2010-06-02 00:00', '2008-02-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fdryTrapMIB.setRevisionsDescriptions(('Changed the ORGANIZATION, CONTACT-INFO and DESCRIPTION fields.', 'Initial version, obsoletes the earlier snAgTrpRcvrTable.',))
if mibBuilder.loadTexts: fdryTrapMIB.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: fdryTrapMIB.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: fdryTrapMIB.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: fdryTrapMIB.setDescription("The Brocade proprietary MIB module for Traps. It has new table combines Ipv4 and Ipv6 configuration of trap Receiver/managers which to send traps. Copyright 1996-2010 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
class SecurityModel(TextualConvention, Integer32):
    description = 'Represents version of trap format to be used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("v1", 1), ("v2c", 2), ("usm", 3))

class SecurityLevel(TextualConvention, Integer32):
    description = 'Represents security levels to be used.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noAuth", 1), ("auth", 2), ("authPriv", 3))

fdryTrapReceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1))
fdryTrapReceiverTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1), )
if mibBuilder.loadTexts: fdryTrapReceiverTable.setStatus('current')
if mibBuilder.loadTexts: fdryTrapReceiverTable.setDescription('Trap Receiver table.')
fdryTrapReceiverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1), ).setIndexNames((0, "FDRY-TRAP-MIB", "fdryTrapReceiverIndex"))
if mibBuilder.loadTexts: fdryTrapReceiverEntry.setStatus('current')
if mibBuilder.loadTexts: fdryTrapReceiverEntry.setDescription('An entry in the Trap Receiver table. This table uses running index as the Index to the table. Reasons to go for running index Scheme than IP addresses: 1. The table will be Virtual Routing and Forwarding(VRF) independent that multiple VRFs could share the same address type and address. 2. Index with address type and address could be potentially 17 unsigned integer, parsing and finding next index takes CPU time. The PDU gets to be huge too! 3. IP address is just another attribute, they are supposed to be list of servers.')
fdryTrapReceiverIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: fdryTrapReceiverIndex.setStatus('current')
if mibBuilder.loadTexts: fdryTrapReceiverIndex.setDescription('The index to the Trap Receiver Table.')
fdryTrapReceiverAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverAddrType.setStatus('current')
if mibBuilder.loadTexts: fdryTrapReceiverAddrType.setDescription('Trap Receiver IP address Type. Supported address types are ipv4(1) and ipv6(2)')
fdryTrapReceiverAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverAddr.setStatus('current')
if mibBuilder.loadTexts: fdryTrapReceiverAddr.setDescription('Trap Receiver IP address.')
fdryTrapReceiverCommunityOrSecurityName = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverCommunityOrSecurityName.setStatus('current')
if mibBuilder.loadTexts: fdryTrapReceiverCommunityOrSecurityName.setDescription('Community string to use. In case of USM (SNMPv3) security model, this object is used to provide the security name.')
fdryTrapReceiverUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(162)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverUDPPort.setStatus('current')
if mibBuilder.loadTexts: fdryTrapReceiverUDPPort.setDescription('UDP port number of the trap receiver.')
fdryTrapReceiverSecurityModel = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 6), SecurityModel().clone('v1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverSecurityModel.setStatus('current')
if mibBuilder.loadTexts: fdryTrapReceiverSecurityModel.setDescription('Version of trap format to be used.')
fdryTrapReceiverSecurityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 7), SecurityLevel().clone('noAuth')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverSecurityLevel.setStatus('current')
if mibBuilder.loadTexts: fdryTrapReceiverSecurityLevel.setDescription('Used for USM (SNMPv3) security model to specify the level of security. The security name is provided by fdryTrapReceiverCommunityOrSecurityName.')
fdryTrapReceiverRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverRowStatus.setStatus('current')
if mibBuilder.loadTexts: fdryTrapReceiverRowStatus.setDescription('This variable is used to create, modify, or delete a row in this table. When a row in this table is in active(1) state, no objects in that row can be modified except this object. ')
mibBuilder.exportSymbols("FDRY-TRAP-MIB", fdryTrapReceiverSecurityLevel=fdryTrapReceiverSecurityLevel, fdryTrapReceiverIndex=fdryTrapReceiverIndex, fdryTrapReceiverAddr=fdryTrapReceiverAddr, fdryTrapReceiverEntry=fdryTrapReceiverEntry, fdryTrapReceiverRowStatus=fdryTrapReceiverRowStatus, SecurityLevel=SecurityLevel, fdryTrapReceiver=fdryTrapReceiver, SecurityModel=SecurityModel, fdryTrapMIB=fdryTrapMIB, fdryTrapReceiverTable=fdryTrapReceiverTable, PYSNMP_MODULE_ID=fdryTrapMIB, fdryTrapReceiverAddrType=fdryTrapReceiverAddrType, fdryTrapReceiverCommunityOrSecurityName=fdryTrapReceiverCommunityOrSecurityName, fdryTrapReceiverUDPPort=fdryTrapReceiverUDPPort, fdryTrapReceiverSecurityModel=fdryTrapReceiverSecurityModel)
