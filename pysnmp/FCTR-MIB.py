#
# PySNMP MIB module FCTR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/FCTR-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:59:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, ObjectIdentity, Unsigned32, IpAddress, MibIdentifier, Counter64, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, enterprises, NotificationType, Counter32, TimeTicks, Gauge32, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "ObjectIdentity", "Unsigned32", "IpAddress", "MibIdentifier", "Counter64", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "enterprises", "NotificationType", "Counter32", "TimeTicks", "Gauge32", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class RequestedFlowControlMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2), ("auto", 3))

class GrantedFlowControlMode(Integer32):
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("disabled", 1), ("flowControl", 2), ("backPressure", 3), ("other", 4))

nbase = MibIdentifier((1, 3, 6, 1, 4, 1, 629))
nbSwitchG1 = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1))
nbSwitchG1Il = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50))
nbFctr = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 2))
nbFctrInfo = MibIdentifier((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1))
nbFctrMgmtType = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("nonControl", 1), ("perDeviceOnly", 2), ("perPort", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbFctrMgmtType.setStatus('mandatory')
nbFctrGlbReqRun = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1, 2), RequestedFlowControlMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbFctrGlbReqRun.setStatus('mandatory')
nbFctrGlbGrntdRun = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1, 3), GrantedFlowControlMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbFctrGlbGrntdRun.setStatus('mandatory')
nbFctrGlbReqPerm = MibScalar((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 1, 4), RequestedFlowControlMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbFctrGlbReqPerm.setStatus('mandatory')
nbFctrPortsTable = MibTable((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2), )
if mibBuilder.loadTexts: nbFctrPortsTable.setStatus('mandatory')
nbFctrPortEntry = MibTableRow((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1), ).setIndexNames((0, "FCTR-MIB", "nbFctrPort"))
if mibBuilder.loadTexts: nbFctrPortEntry.setStatus('mandatory')
nbFctrPort = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbFctrPort.setStatus('mandatory')
nbFctrPortRunReqMode = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1, 2), RequestedFlowControlMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbFctrPortRunReqMode.setStatus('mandatory')
nbFctrPortRunGrntd = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1, 3), GrantedFlowControlMode()).setMaxAccess("readonly")
if mibBuilder.loadTexts: nbFctrPortRunGrntd.setStatus('mandatory')
nbFctrPortPermReqMode = MibTableColumn((1, 3, 6, 1, 4, 1, 629, 1, 50, 2, 2, 1, 4), RequestedFlowControlMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: nbFctrPortPermReqMode.setStatus('mandatory')
mibBuilder.exportSymbols("FCTR-MIB", nbFctrPortRunGrntd=nbFctrPortRunGrntd, nbFctr=nbFctr, nbFctrPort=nbFctrPort, nbFctrPortRunReqMode=nbFctrPortRunReqMode, RequestedFlowControlMode=RequestedFlowControlMode, nbFctrMgmtType=nbFctrMgmtType, nbFctrGlbReqPerm=nbFctrGlbReqPerm, nbFctrPortEntry=nbFctrPortEntry, nbFctrPortsTable=nbFctrPortsTable, nbFctrGlbGrntdRun=nbFctrGlbGrntdRun, nbSwitchG1=nbSwitchG1, nbase=nbase, nbFctrGlbReqRun=nbFctrGlbReqRun, nbSwitchG1Il=nbSwitchG1Il, nbFctrPortPermReqMode=nbFctrPortPermReqMode, nbFctrInfo=nbFctrInfo, GrantedFlowControlMode=GrantedFlowControlMode)
