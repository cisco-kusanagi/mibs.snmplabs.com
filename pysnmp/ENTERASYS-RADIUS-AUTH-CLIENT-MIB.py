#
# PySNMP MIB module ENTERASYS-RADIUS-AUTH-CLIENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ENTERASYS-RADIUS-AUTH-CLIENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:50:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
etsysModules, = mibBuilder.importSymbols("ENTERASYS-MIB-NAMES", "etsysModules")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter64, ObjectIdentity, ModuleIdentity, Integer32, Bits, iso, TimeTicks, Gauge32, NotificationType, IpAddress, Unsigned32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter64", "ObjectIdentity", "ModuleIdentity", "Integer32", "Bits", "iso", "TimeTicks", "Gauge32", "NotificationType", "IpAddress", "Unsigned32", "Counter32")
TruthValue, TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString", "RowStatus")
etsysRadiusAuthClientMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4))
etsysRadiusAuthClientMIB.setRevisions(('2011-06-29 17:14', '2009-08-06 18:38', '2005-07-29 13:48', '2004-07-27 19:53', '2003-11-06 18:23', '2002-01-24 15:57', '2000-11-08 00:00',))
if mibBuilder.loadTexts: etsysRadiusAuthClientMIB.setLastUpdated('201106291714Z')
if mibBuilder.loadTexts: etsysRadiusAuthClientMIB.setOrganization('Enterasys Networks, Inc')
etsysRadiusAuthClientMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1))
etsysRadiusAuthClientRetryTimeout = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setUnits('seconds').setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRadiusAuthClientRetryTimeout.setStatus('current')
etsysRadiusAuthClientRetries = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRadiusAuthClientRetries.setStatus('current')
etsysRadiusAuthClientEnable = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRadiusAuthClientEnable.setStatus('current')
etsysRadiusAuthClientAuthType = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("mac", 1), ("eapol", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRadiusAuthClientAuthType.setStatus('deprecated')
etsysRadiusAuthServerTable = MibTable((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5), )
if mibBuilder.loadTexts: etsysRadiusAuthServerTable.setStatus('current')
etsysRadiusAuthServerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1), ).setIndexNames((0, "ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthServerIndex"))
if mibBuilder.loadTexts: etsysRadiusAuthServerEntry.setStatus('current')
etsysRadiusAuthServerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647)))
if mibBuilder.loadTexts: etsysRadiusAuthServerIndex.setStatus('current')
etsysRadiusAuthClientServerAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 2), InetAddressType().clone('ipv4')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerAddressType.setStatus('current')
etsysRadiusAuthClientServerAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 3), InetAddress().subtype(subtypeSpec=ValueSizeConstraint(1, 64))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerAddress.setStatus('current')
etsysRadiusAuthClientServerPortNumber = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(1812)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerPortNumber.setStatus('current')
etsysRadiusAuthClientServerSecret = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerSecret.setStatus('current')
etsysRadiusAuthClientServerSecretEntered = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 6), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerSecretEntered.setStatus('current')
etsysRadiusAuthClientServerClearTime = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 2147483647))).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerClearTime.setStatus('deprecated')
etsysRadiusAuthClientServerStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerStatus.setStatus('current')
etsysRadiusAuthClientServerRealmType = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("any", 1), ("mgmtAccess", 2), ("networkAccess", 3))).clone('any')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerRealmType.setStatus('current')
etsysRadiusAuthClientServerTimeout = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 60), )).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerTimeout.setStatus('current')
etsysRadiusAuthClientServerRetries = MibTableColumn((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 5, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(1, 10), )).clone(-1)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: etsysRadiusAuthClientServerRetries.setStatus('current')
etsysRadiusAuthClientAttrMgmtPassword = MibScalar((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("standard", 1), ("mschapv2", 2)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: etsysRadiusAuthClientAttrMgmtPassword.setStatus('current')
etsysRadiusAuthClientMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2))
etsysRadiusAuthClientMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 1))
etsysRadiusAuthClientMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 2))
etsysRadiusAuthClientMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 2, 1)).setObjects(("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetryTimeout"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetries"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientEnable"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientAuthType"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddressType"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddress"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerPortNumber"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecret"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecretEntered"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerClearTime"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRadiusAuthClientMIBGroup = etsysRadiusAuthClientMIBGroup.setStatus('deprecated')
etsysRadiusAuthClientMIBGroupV2 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 2, 2)).setObjects(("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetryTimeout"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetries"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientEnable"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddressType"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddress"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerPortNumber"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecret"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecretEntered"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerStatus"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerRealmType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRadiusAuthClientMIBGroupV2 = etsysRadiusAuthClientMIBGroupV2.setStatus('deprecated')
etsysRadiusAuthClientMIBGroupV3 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 2, 3)).setObjects(("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetryTimeout"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetries"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientEnable"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddressType"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddress"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerPortNumber"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecret"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecretEntered"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerStatus"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerRealmType"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerTimeout"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerRetries"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRadiusAuthClientMIBGroupV3 = etsysRadiusAuthClientMIBGroupV3.setStatus('deprecated')
etsysRadiusAuthClientMIBGroupV4 = ObjectGroup((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 2, 4)).setObjects(("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetryTimeout"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientRetries"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientEnable"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddressType"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerAddress"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerPortNumber"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecret"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerSecretEntered"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerStatus"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerRealmType"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerTimeout"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientServerRetries"), ("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientAttrMgmtPassword"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRadiusAuthClientMIBGroupV4 = etsysRadiusAuthClientMIBGroupV4.setStatus('current')
etsysRadiusClientMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 1, 1)).setObjects(("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRadiusClientMIBCompliance = etsysRadiusClientMIBCompliance.setStatus('deprecated')
etsysRadiusClientMIBComplianceV2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 1, 2)).setObjects(("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientMIBGroupV2"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRadiusClientMIBComplianceV2 = etsysRadiusClientMIBComplianceV2.setStatus('deprecated')
etsysRadiusClientMIBComplianceV3 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 1, 3)).setObjects(("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientMIBGroupV3"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRadiusClientMIBComplianceV3 = etsysRadiusClientMIBComplianceV3.setStatus('deprecated')
etsysRadiusClientMIBComplianceV4 = ModuleCompliance((1, 3, 6, 1, 4, 1, 5624, 1, 2, 4, 2, 1, 4)).setObjects(("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", "etsysRadiusAuthClientMIBGroupV4"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    etsysRadiusClientMIBComplianceV4 = etsysRadiusClientMIBComplianceV4.setStatus('current')
mibBuilder.exportSymbols("ENTERASYS-RADIUS-AUTH-CLIENT-MIB", etsysRadiusAuthServerTable=etsysRadiusAuthServerTable, etsysRadiusAuthClientMIBGroup=etsysRadiusAuthClientMIBGroup, etsysRadiusAuthClientAuthType=etsysRadiusAuthClientAuthType, PYSNMP_MODULE_ID=etsysRadiusAuthClientMIB, etsysRadiusAuthClientServerClearTime=etsysRadiusAuthClientServerClearTime, etsysRadiusAuthClientServerTimeout=etsysRadiusAuthClientServerTimeout, etsysRadiusAuthClientMIBObjects=etsysRadiusAuthClientMIBObjects, etsysRadiusAuthClientMIBGroupV3=etsysRadiusAuthClientMIBGroupV3, etsysRadiusAuthClientMIBGroups=etsysRadiusAuthClientMIBGroups, etsysRadiusAuthServerIndex=etsysRadiusAuthServerIndex, etsysRadiusAuthClientServerAddress=etsysRadiusAuthClientServerAddress, etsysRadiusAuthClientServerSecret=etsysRadiusAuthClientServerSecret, etsysRadiusAuthClientMIBGroupV4=etsysRadiusAuthClientMIBGroupV4, etsysRadiusAuthClientMIBConformance=etsysRadiusAuthClientMIBConformance, etsysRadiusAuthClientMIBCompliances=etsysRadiusAuthClientMIBCompliances, etsysRadiusAuthServerEntry=etsysRadiusAuthServerEntry, etsysRadiusAuthClientRetries=etsysRadiusAuthClientRetries, etsysRadiusAuthClientServerRetries=etsysRadiusAuthClientServerRetries, etsysRadiusClientMIBComplianceV3=etsysRadiusClientMIBComplianceV3, etsysRadiusAuthClientServerPortNumber=etsysRadiusAuthClientServerPortNumber, etsysRadiusClientMIBComplianceV4=etsysRadiusClientMIBComplianceV4, etsysRadiusAuthClientServerAddressType=etsysRadiusAuthClientServerAddressType, etsysRadiusAuthClientServerStatus=etsysRadiusAuthClientServerStatus, etsysRadiusAuthClientMIB=etsysRadiusAuthClientMIB, etsysRadiusAuthClientMIBGroupV2=etsysRadiusAuthClientMIBGroupV2, etsysRadiusClientMIBCompliance=etsysRadiusClientMIBCompliance, etsysRadiusAuthClientServerSecretEntered=etsysRadiusAuthClientServerSecretEntered, etsysRadiusClientMIBComplianceV2=etsysRadiusClientMIBComplianceV2, etsysRadiusAuthClientServerRealmType=etsysRadiusAuthClientServerRealmType, etsysRadiusAuthClientRetryTimeout=etsysRadiusAuthClientRetryTimeout, etsysRadiusAuthClientAttrMgmtPassword=etsysRadiusAuthClientAttrMgmtPassword, etsysRadiusAuthClientEnable=etsysRadiusAuthClientEnable)
