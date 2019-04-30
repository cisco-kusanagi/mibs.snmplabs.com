#
# PySNMP MIB module FDRY-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FDRY-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:59:46 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
fdryTrap, = mibBuilder.importSymbols("FOUNDRY-SN-ROOT-MIB", "fdryTrap")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ModuleIdentity, TimeTicks, NotificationType, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, ObjectIdentity, IpAddress, Integer32, iso, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "TimeTicks", "NotificationType", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "ObjectIdentity", "IpAddress", "Integer32", "iso", "Bits", "Gauge32")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
fdryTrapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1))
fdryTrapMIB.setRevisions(('2010-06-02 00:00', '2008-02-25 00:00',))
if mibBuilder.loadTexts: fdryTrapMIB.setLastUpdated('201006020000Z')
if mibBuilder.loadTexts: fdryTrapMIB.setOrganization('Brocade Communications Systems, Inc.')
class SecurityModel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("v1", 1), ("v2c", 2), ("usm", 3))

class SecurityLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("noAuth", 1), ("auth", 2), ("authPriv", 3))

fdryTrapReceiver = MibIdentifier((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1))
fdryTrapReceiverTable = MibTable((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1), )
if mibBuilder.loadTexts: fdryTrapReceiverTable.setStatus('current')
fdryTrapReceiverEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1), ).setIndexNames((0, "FDRY-TRAP-MIB", "fdryTrapReceiverIndex"))
if mibBuilder.loadTexts: fdryTrapReceiverEntry.setStatus('current')
fdryTrapReceiverIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 1), Unsigned32())
if mibBuilder.loadTexts: fdryTrapReceiverIndex.setStatus('current')
fdryTrapReceiverAddrType = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverAddrType.setStatus('current')
fdryTrapReceiverAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 3), InetAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverAddr.setStatus('current')
fdryTrapReceiverCommunityOrSecurityName = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverCommunityOrSecurityName.setStatus('current')
fdryTrapReceiverUDPPort = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 5), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(162)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverUDPPort.setStatus('current')
fdryTrapReceiverSecurityModel = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 6), SecurityModel().clone('v1')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverSecurityModel.setStatus('current')
fdryTrapReceiverSecurityLevel = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 7), SecurityLevel().clone('noAuth')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverSecurityLevel.setStatus('current')
fdryTrapReceiverRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1991, 1, 1, 10, 1, 1, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: fdryTrapReceiverRowStatus.setStatus('current')
mibBuilder.exportSymbols("FDRY-TRAP-MIB", fdryTrapReceiverUDPPort=fdryTrapReceiverUDPPort, fdryTrapReceiverAddr=fdryTrapReceiverAddr, fdryTrapReceiver=fdryTrapReceiver, fdryTrapReceiverAddrType=fdryTrapReceiverAddrType, PYSNMP_MODULE_ID=fdryTrapMIB, fdryTrapMIB=fdryTrapMIB, SecurityLevel=SecurityLevel, fdryTrapReceiverCommunityOrSecurityName=fdryTrapReceiverCommunityOrSecurityName, fdryTrapReceiverSecurityModel=fdryTrapReceiverSecurityModel, fdryTrapReceiverRowStatus=fdryTrapReceiverRowStatus, fdryTrapReceiverSecurityLevel=fdryTrapReceiverSecurityLevel, fdryTrapReceiverIndex=fdryTrapReceiverIndex, fdryTrapReceiverTable=fdryTrapReceiverTable, SecurityModel=SecurityModel, fdryTrapReceiverEntry=fdryTrapReceiverEntry)
