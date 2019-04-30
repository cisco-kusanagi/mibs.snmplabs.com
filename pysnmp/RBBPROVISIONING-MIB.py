#
# PySNMP MIB module RBBPROVISIONING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBBPROVISIONING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:43:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
AtmConnCastType, AtmVcIdentifier, AtmServiceCategory, AtmAddr, AtmVpIdentifier, AtmConnKind, AtmTrafficDescrParamIndex = mibBuilder.importSymbols("ATM-TC-MIB", "AtmConnCastType", "AtmVcIdentifier", "AtmServiceCategory", "AtmAddr", "AtmVpIdentifier", "AtmConnKind", "AtmTrafficDescrParamIndex")
ifIndex, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "ifIndex", "InterfaceIndex")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Gauge32, TimeTicks, Counter64, enterprises, ModuleIdentity, IpAddress, Integer32, Bits, MibIdentifier, mib_2, ObjectIdentity, Unsigned32, Counter32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "Counter64", "enterprises", "ModuleIdentity", "IpAddress", "Integer32", "Bits", "MibIdentifier", "mib-2", "ObjectIdentity", "Unsigned32", "Counter32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
rbbProvMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 4839, 32))
if mibBuilder.loadTexts: rbbProvMIB.setLastUpdated('9909271200Z')
if mibBuilder.loadTexts: rbbProvMIB.setOrganization('IETF ADSL MIB Working Group')
class RBBServiceID(TextualConvention, ObjectIdentifier):
    status = 'current'

class RBBServiceName(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class RBBServiceProvider(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class RBBServiceStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("other", 1), ("up", 2), ("down", 3), ("adminDown", 4))

class RBBURLType(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 128)

class RBBCPEAuthType(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class RBBMailAddr(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class RBBCPESerialNumber(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 32)

class RBBVendorModel(DisplayString):
    status = 'current'
    subtypeSpec = DisplayString.subtypeSpec + ValueSizeConstraint(0, 64)

class RowStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("active", 1), ("notInService", 2), ("notReady", 3), ("createAndGo", 4), ("createAndWait", 5), ("destroy", 6))

rbbProvMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 4839, 32, 1))
rbbServicesGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1))
rbbSubGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4839, 32, 1, 2))
rbbCPEGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3))
rbbVendorGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4839, 32, 1, 4))
rbbNotifyGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 4839, 32, 1, 12))
srvServicesTable = MibTable((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1), )
if mibBuilder.loadTexts: srvServicesTable.setStatus('current')
srvServiceEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1), ).setIndexNames((0, "RBBPROVISIONING-MIB", "srvServiceIdentifier"))
if mibBuilder.loadTexts: srvServiceEntry.setStatus('current')
srvServiceIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 1), RBBServiceID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: srvServiceIdentifier.setStatus('current')
srvServiceName = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 2), RBBServiceName()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: srvServiceName.setStatus('current')
srvServiceProvider = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 3), RBBServiceProvider()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: srvServiceProvider.setStatus('current')
srvServiceStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 4), RBBServiceStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: srvServiceStatus.setStatus('current')
srvServiceConnType = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 5), AtmConnKind()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: srvServiceConnType.setStatus('current')
srvServiceQOSType = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: srvServiceQOSType.setStatus('current')
srvServiceSpeedReq = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 7), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: srvServiceSpeedReq.setStatus('current')
srvServiceLatencyReq = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("high", 1), ("med", 2), ("low", 3)))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: srvServiceLatencyReq.setStatus('current')
srvServiceURL = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 9), RBBURLType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: srvServiceURL.setStatus('current')
srvServiceDescr = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 10), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: srvServiceDescr.setStatus('current')
srvAdminContact = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 11), RBBMailAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: srvAdminContact.setStatus('current')
srvRowInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 1, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: srvRowInfo.setStatus('current')
rbbSubTable = MibTable((1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1), )
if mibBuilder.loadTexts: rbbSubTable.setStatus('current')
rbbSubEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1), ).setIndexNames((0, "RBBPROVISIONING-MIB", "rbbSubVendor"), (0, "RBBPROVISIONING-MIB", "rbbSubModel"), (0, "RBBPROVISIONING-MIB", "rbbSubSerialNumber"), (0, "RBBPROVISIONING-MIB", "rbbSubServiceIdentifier"))
if mibBuilder.loadTexts: rbbSubEntry.setStatus('current')
rbbSubVendor = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 1), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbSubVendor.setStatus('current')
rbbSubModel = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 3), RBBVendorModel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbSubModel.setStatus('current')
rbbSubSerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 4), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbSubSerialNumber.setStatus('current')
rbbSubServiceIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 5), RBBServiceID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbSubServiceIdentifier.setStatus('current')
rbbSubVPI = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 6), AtmVpIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbSubVPI.setStatus('current')
rbbSubVCI = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 7), AtmVcIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbSubVCI.setStatus('current')
rbbSubAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 8), AtmAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbSubAddr.setStatus('current')
rbbSubStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 9), RBBServiceStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbSubStatus.setStatus('current')
rbbSubRowInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 2, 1, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbSubRowInfo.setStatus('current')
rbbCPETable = MibTable((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1), )
if mibBuilder.loadTexts: rbbCPETable.setStatus('current')
rbbCPEEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1), ).setIndexNames((0, "RBBPROVISIONING-MIB", "rbbVendorOID"), (0, "RBBPROVISIONING-MIB", "rbbVendorModel"), (0, "RBBPROVISIONING-MIB", "rbbCPESerialNumber"))
if mibBuilder.loadTexts: rbbCPEEntry.setStatus('current')
rbbCPEAuthValue = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 1), RBBCPEAuthType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbCPEAuthValue.setStatus('current')
rbbCPEVendorOID = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 2), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbCPEVendorOID.setStatus('current')
rbbCPEVendorModel = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 3), RBBVendorModel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbCPEVendorModel.setStatus('current')
rbbCPEStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 4), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbCPEStatus.setStatus('current')
rbbCPESubCount = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbCPESubCount.setStatus('current')
rbbCPESubAggrSpeed = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 6), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbCPESubAggrSpeed.setStatus('current')
rbbCPECustContact = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 7), RBBMailAddr()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbCPECustContact.setStatus('current')
rbbCPESerialNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 8), RBBCPESerialNumber()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbCPESerialNumber.setStatus('current')
rbbCPETrapEnable = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 9), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbCPETrapEnable.setStatus('current')
rbbCPECurrentImage = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 10), RBBURLType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbCPECurrentImage.setStatus('current')
rbbCPEIpAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 11), IpAddress()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbCPEIpAddress.setStatus('current')
rbbCPERowInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 3, 1, 1, 12), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbCPERowInfo.setStatus('current')
rbbVendorTable = MibTable((1, 3, 6, 1, 4, 1, 4839, 32, 1, 4, 1), )
if mibBuilder.loadTexts: rbbVendorTable.setStatus('current')
rbbVendorEntry = MibTableRow((1, 3, 6, 1, 4, 1, 4839, 32, 1, 4, 1, 1), ).setIndexNames((0, "RBBPROVISIONING-MIB", "rbbVendorOID"), (0, "RBBPROVISIONING-MIB", "rbbVendorModel"))
if mibBuilder.loadTexts: rbbVendorEntry.setStatus('current')
rbbVendorOID = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 4, 1, 1, 1), ObjectIdentifier()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbVendorOID.setStatus('current')
rbbVendorModel = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 4, 1, 1, 2), RBBVendorModel()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbVendorModel.setStatus('current')
rbbVendorImageURL = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 4, 1, 1, 3), RBBURLType()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbVendorImageURL.setStatus('current')
rbbVendorRowInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 4839, 32, 1, 4, 1, 1, 4), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rbbVendorRowInfo.setStatus('current')
rbbSrvGrpSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 4839, 32, 1, 5), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbbSrvGrpSerialNumber.setStatus('current')
rbbSubGrpSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 4839, 32, 1, 6), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbbSubGrpSerialNumber.setStatus('current')
rbbCPEGrpSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 4839, 32, 1, 7), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbbCPEGrpSerialNumber.setStatus('current')
rbbVendorGrpSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 4839, 32, 1, 8), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rbbVendorGrpSerialNumber.setStatus('current')
rbbSubNotify = NotificationType((1, 3, 6, 1, 4, 1, 4839, 32, 1, 12, 1)).setObjects(("RBBPROVISIONING-MIB", "rbbSubVendor"), ("RBBPROVISIONING-MIB", "rbbSubModel"), ("RBBPROVISIONING-MIB", "rbbSubSerialNumber"), ("RBBPROVISIONING-MIB", "rbbSubServiceIdentifier"))
if mibBuilder.loadTexts: rbbSubNotify.setStatus('current')
rbbPowerUpNotify = NotificationType((1, 3, 6, 1, 4, 1, 4839, 32, 1, 12, 2)).setObjects(("RBBPROVISIONING-MIB", "rbbCPEVendorOID"), ("RBBPROVISIONING-MIB", "rbbCPEVendorModel"), ("RBBPROVISIONING-MIB", "rbbCPESerialNumber"))
if mibBuilder.loadTexts: rbbPowerUpNotify.setStatus('current')
mibBuilder.exportSymbols("RBBPROVISIONING-MIB", srvAdminContact=srvAdminContact, srvServiceQOSType=srvServiceQOSType, RBBURLType=RBBURLType, srvServiceURL=srvServiceURL, rbbVendorGrpSerialNumber=rbbVendorGrpSerialNumber, RBBServiceName=RBBServiceName, rbbCPETable=rbbCPETable, RBBServiceID=RBBServiceID, rbbVendorGroup=rbbVendorGroup, rbbSubAddr=rbbSubAddr, RBBVendorModel=RBBVendorModel, rbbSubStatus=rbbSubStatus, rbbCPETrapEnable=rbbCPETrapEnable, rbbCPECurrentImage=rbbCPECurrentImage, rbbCPEVendorOID=rbbCPEVendorOID, rbbCPEStatus=rbbCPEStatus, rbbVendorTable=rbbVendorTable, rbbCPESubAggrSpeed=rbbCPESubAggrSpeed, rbbProvMIB=rbbProvMIB, rbbVendorModel=rbbVendorModel, rbbVendorImageURL=rbbVendorImageURL, srvServiceSpeedReq=srvServiceSpeedReq, rbbCPESerialNumber=rbbCPESerialNumber, rbbSubVCI=rbbSubVCI, rbbSubVendor=rbbSubVendor, rbbVendorEntry=rbbVendorEntry, rbbCPEIpAddress=rbbCPEIpAddress, rbbSubGrpSerialNumber=rbbSubGrpSerialNumber, rbbVendorRowInfo=rbbVendorRowInfo, srvServiceIdentifier=srvServiceIdentifier, rbbServicesGroup=rbbServicesGroup, srvServicesTable=srvServicesTable, srvServiceDescr=srvServiceDescr, rbbSubGroup=rbbSubGroup, srvServiceName=srvServiceName, rbbSubRowInfo=rbbSubRowInfo, RBBCPESerialNumber=RBBCPESerialNumber, rbbSubServiceIdentifier=rbbSubServiceIdentifier, rbbCPESubCount=rbbCPESubCount, rbbSrvGrpSerialNumber=rbbSrvGrpSerialNumber, rbbCPEGrpSerialNumber=rbbCPEGrpSerialNumber, srvServiceConnType=srvServiceConnType, RBBMailAddr=RBBMailAddr, RowStatus=RowStatus, srvRowInfo=srvRowInfo, srvServiceEntry=srvServiceEntry, srvServiceStatus=srvServiceStatus, rbbSubEntry=rbbSubEntry, rbbSubModel=rbbSubModel, rbbCPEEntry=rbbCPEEntry, rbbSubNotify=rbbSubNotify, rbbCPECustContact=rbbCPECustContact, rbbCPEGroup=rbbCPEGroup, srvServiceProvider=srvServiceProvider, rbbPowerUpNotify=rbbPowerUpNotify, rbbVendorOID=rbbVendorOID, RBBServiceStatus=RBBServiceStatus, PYSNMP_MODULE_ID=rbbProvMIB, srvServiceLatencyReq=srvServiceLatencyReq, rbbSubVPI=rbbSubVPI, rbbCPEVendorModel=rbbCPEVendorModel, rbbProvMIBObjects=rbbProvMIBObjects, rbbNotifyGroup=rbbNotifyGroup, rbbCPERowInfo=rbbCPERowInfo, rbbCPEAuthValue=rbbCPEAuthValue, RBBCPEAuthType=RBBCPEAuthType, RBBServiceProvider=RBBServiceProvider, rbbSubSerialNumber=rbbSubSerialNumber, rbbSubTable=rbbSubTable)
