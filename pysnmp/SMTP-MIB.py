#
# PySNMP MIB module SMTP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SMTP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:59:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
dlink_common_mgmt, = mibBuilder.importSymbols("DLINK-ID-REC-MIB", "dlink-common-mgmt")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, Counter32, MibIdentifier, Integer32, Unsigned32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter64, ObjectIdentity, NotificationType, Bits, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "MibIdentifier", "Integer32", "Unsigned32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter64", "ObjectIdentity", "NotificationType", "Bits", "ModuleIdentity", "IpAddress")
RowStatus, DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "RowStatus", "DisplayString", "TextualConvention")
swSMTPMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 171, 12, 29))
if mibBuilder.loadTexts: swSMTPMIB.setLastUpdated('0007150000Z')
if mibBuilder.loadTexts: swSMTPMIB.setOrganization(' ')
class VlanId(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 4094)

class PortList(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 127)

class MacAddress(OctetString):
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

swSMTPCtrl = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 29, 1))
swSMTPInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 29, 2))
swSMTPMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 171, 12, 29, 3))
smtpStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("disabled", 2), ("enabled", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpStatus.setStatus('current')
smtpSrvAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpSrvAddr.setStatus('current')
smtpSrvPort = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpSrvPort.setStatus('current')
smtpSelfMailAddr = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpSelfMailAddr.setStatus('current')
smtpTestMsgSubject = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 5), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 128))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpTestMsgSubject.setStatus('current')
smtpTestMsgContent = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 6), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 512))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpTestMsgContent.setStatus('current')
smtpSendTestMsg = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("send", 1), ("noAction", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: smtpSendTestMsg.setStatus('current')
smtpSendTestStatus = MibScalar((1, 3, 6, 1, 4, 1, 171, 12, 29, 2, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("success", 1), ("failed", 2), ("in-processing", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smtpSendTestStatus.setStatus('current')
smtpMailReceiverTable = MibTable((1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1), )
if mibBuilder.loadTexts: smtpMailReceiverTable.setStatus('current')
smtpReceiverAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1, 1), ).setIndexNames((0, "SMTP-MIB", "smtpMailReceiverAddrIndex"))
if mibBuilder.loadTexts: smtpReceiverAddrEntry.setStatus('current')
smtpMailReceiverAddrIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 8))).setMaxAccess("readonly")
if mibBuilder.loadTexts: smtpMailReceiverAddrIndex.setStatus('current')
smtpMailReceiverAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smtpMailReceiverAddr.setStatus('current')
smtpMailReceiverAddrState = MibTableColumn((1, 3, 6, 1, 4, 1, 171, 12, 29, 3, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: smtpMailReceiverAddrState.setStatus('current')
mibBuilder.exportSymbols("SMTP-MIB", smtpMailReceiverTable=smtpMailReceiverTable, VlanId=VlanId, smtpStatus=smtpStatus, swSMTPMgmt=swSMTPMgmt, swSMTPMIB=swSMTPMIB, smtpSendTestMsg=smtpSendTestMsg, PYSNMP_MODULE_ID=swSMTPMIB, smtpMailReceiverAddrState=smtpMailReceiverAddrState, smtpTestMsgContent=smtpTestMsgContent, smtpSrvPort=smtpSrvPort, swSMTPCtrl=swSMTPCtrl, smtpSelfMailAddr=smtpSelfMailAddr, MacAddress=MacAddress, swSMTPInfo=swSMTPInfo, smtpReceiverAddrEntry=smtpReceiverAddrEntry, smtpMailReceiverAddr=smtpMailReceiverAddr, PortList=PortList, smtpSrvAddr=smtpSrvAddr, smtpTestMsgSubject=smtpTestMsgSubject, smtpMailReceiverAddrIndex=smtpMailReceiverAddrIndex, smtpSendTestStatus=smtpSendTestStatus)
