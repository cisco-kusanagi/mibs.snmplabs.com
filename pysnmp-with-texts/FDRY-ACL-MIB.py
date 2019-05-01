#
# PySNMP MIB module FDRY-ACL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FDRY-ACL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:13:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
fdryAcl, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "fdryAcl")
Ipv6Address, = mibBuilder.importSymbols("IPV6-TC", "Ipv6Address")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, TimeTicks, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, Integer32, Counter32, NotificationType, Bits, Gauge32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "TimeTicks", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "Integer32", "Counter32", "NotificationType", "Bits", "Gauge32", "IpAddress")
TextualConvention, DisplayString, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue", "RowStatus")
fdryAclMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1))
fdryAclMIB.setRevisions(('2010-06-02 00:00', '2008-02-14 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: fdryAclMIB.setRevisionsDescriptions(('Changed the ORGANIZATION, CONTACT-INFO and DESCRIPTION fields.', 'Initial version',))
if mibBuilder.loadTexts: fdryAclMIB.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: fdryAclMIB.setOrganization('Brocade Communications Systems, Inc.')
if mibBuilder.loadTexts: fdryAclMIB.setContactInfo('Technical Support Center 130 Holger Way, San Jose, CA 95134 Email: ipsupport@brocade.com Phone: 1-800-752-8061 URL: www.brocade.com')
if mibBuilder.loadTexts: fdryAclMIB.setDescription("The Brocade proprietary MIB module for Ipv6 Access Control List. It has new tables for Ipv6 Access Control List. Copyright 1996-2010 Brocade Communications Systems, Inc. All rights reserved. This Brocade Communications Systems SNMP Management Information Base Specification embodies Brocade Communications Systems' confidential and proprietary intellectual property. Brocade Communications Systems retains all title and ownership in the Specification, including any revisions. This Specification is supplied AS IS, and Brocade Communications Systems makes no warranty, either express or implied, as to the use, operation, condition, or performance of the specification, and any unintended consequence it may on the user environment.")
class RtrStatus(TextualConvention, Integer32):
    description = 'Represents a status value such as disabled or enabled.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("disabled", 0), ("enabled", 1))

class Action(TextualConvention, Integer32):
    description = 'Represents a action value such as deny or permit.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("deny", 0), ("permit", 1))

class Operator(TextualConvention, Integer32):
    description = 'Represents a operators value, such as equal, not-equal, lesser than, greater than, range and undefined.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 7))
    namedValues = NamedValues(("eq", 0), ("neq", 1), ("lt", 2), ("gt", 3), ("range", 4), ("undefined", 7))

class IpProtocol(TextualConvention, Unsigned32):
    description = 'Represents a transport protocol value.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

fdryIpv6Acl = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1))
fdryIpv6AclTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1), )
if mibBuilder.loadTexts: fdryIpv6AclTable.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclTable.setDescription('Table of Ipv6 Access Control List')
fdryIpv6AclEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1), ).setIndexNames((0, "FDRY-ACL-MIB", "fdryIpv6AclIndex"))
if mibBuilder.loadTexts: fdryIpv6AclEntry.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclEntry.setDescription('An entry in the Ipv6 Access Control List table.')
fdryIpv6AclIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: fdryIpv6AclIndex.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclIndex.setDescription('The access control list item number for an entry. This is a unique number that identifies different Access list entries. This one has to be unique even though the name is not unique for a give access list with same or different source address, prefix length, destination address and destination prefix length, protocol type, action (permit/deny) type and the operator (neq, eq, gt and , lt).')
fdryIpv6AclName = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 199))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclName.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclName.setDescription('Access Control List name for an entry.')
fdryIpv6AclAction = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 3), Action()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclAction.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclAction.setDescription('Action to take if the ip packet matches with this access control list.')
fdryIpv6AclProtocol = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 4), IpProtocol()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclProtocol.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclProtocol.setDescription('Transport protocols. 0 means any protocol.')
fdryIpv6AclSourceIp = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 5), Ipv6Address()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclSourceIp.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclSourceIp.setDescription('Source Ipv6 address.')
fdryIpv6AclSourcePrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 6), Unsigned32().clone(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclSourcePrefixLen.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclSourcePrefixLen.setDescription('Source IPv6 address prefix length.')
fdryIpv6AclSourceOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 7), Operator()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclSourceOperator.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclSourceOperator.setDescription('Type of comparison to perform. for now, this only applys to tcp or udp to compare the port number')
fdryIpv6AclSourceOperand1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclSourceOperand1.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclSourceOperand1.setDescription('For now this only refers to transport protocol port number.')
fdryIpv6AclSourceOperand2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclSourceOperand2.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclSourceOperand2.setDescription('For now this only refers to transport protocol port number.')
fdryIpv6AclDestinationIp = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 10), Ipv6Address()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclDestinationIp.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclDestinationIp.setDescription('Destination Ipv6 address.')
fdryIpv6AclDestinationPrefixLen = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 11), Unsigned32().clone(64)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclDestinationPrefixLen.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclDestinationPrefixLen.setDescription('Destination IPv6 address prefix length.')
fdryIpv6AclDestinationOperator = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 12), Operator()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclDestinationOperator.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclDestinationOperator.setDescription('Type of comparison to perform. for now, this only applys to tcp or udp to compare the port number')
fdryIpv6AclDestinationOperand1 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 13), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclDestinationOperand1.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclDestinationOperand1.setDescription('For now this only refers to transport protocol port number.')
fdryIpv6AclDestinationOperand2 = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 14), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclDestinationOperand2.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclDestinationOperand2.setDescription('For now this only refers to transport protocol port number.')
fdryIpv6AclEstablished = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 15), RtrStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclEstablished.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclEstablished.setDescription('Enable/Disable the filtering of established TCP packets of which the ACK or RESET flag is on. This additional filter only applies to TCP transport protocol.')
fdryIpv6AclLogOption = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 16), TruthValue()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclLogOption.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclLogOption.setDescription('Log flag, should be set to one to enable logging')
fdryIpv6AclComments = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 17), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclComments.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclComments.setDescription('Remark description of individual Access Control List entry.')
fdryIpv6AclRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 2, 16, 1, 1, 1, 1, 18), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryIpv6AclRowStatus.setStatus('current')
if mibBuilder.loadTexts: fdryIpv6AclRowStatus.setDescription('To create or delete a access list entry.')
mibBuilder.exportSymbols("FDRY-ACL-MIB", fdryIpv6AclIndex=fdryIpv6AclIndex, fdryIpv6AclSourceOperand2=fdryIpv6AclSourceOperand2, fdryIpv6AclAction=fdryIpv6AclAction, fdryIpv6AclSourceIp=fdryIpv6AclSourceIp, fdryIpv6AclDestinationOperand2=fdryIpv6AclDestinationOperand2, fdryIpv6AclSourceOperator=fdryIpv6AclSourceOperator, fdryIpv6AclRowStatus=fdryIpv6AclRowStatus, fdryIpv6Acl=fdryIpv6Acl, fdryIpv6AclTable=fdryIpv6AclTable, fdryIpv6AclComments=fdryIpv6AclComments, fdryIpv6AclDestinationOperator=fdryIpv6AclDestinationOperator, fdryIpv6AclProtocol=fdryIpv6AclProtocol, fdryIpv6AclSourcePrefixLen=fdryIpv6AclSourcePrefixLen, fdryIpv6AclDestinationIp=fdryIpv6AclDestinationIp, Operator=Operator, fdryIpv6AclEstablished=fdryIpv6AclEstablished, fdryIpv6AclLogOption=fdryIpv6AclLogOption, Action=Action, fdryIpv6AclDestinationOperand1=fdryIpv6AclDestinationOperand1, fdryIpv6AclDestinationPrefixLen=fdryIpv6AclDestinationPrefixLen, fdryIpv6AclName=fdryIpv6AclName, fdryIpv6AclSourceOperand1=fdryIpv6AclSourceOperand1, RtrStatus=RtrStatus, fdryAclMIB=fdryAclMIB, PYSNMP_MODULE_ID=fdryAclMIB, fdryIpv6AclEntry=fdryIpv6AclEntry, IpProtocol=IpProtocol)
