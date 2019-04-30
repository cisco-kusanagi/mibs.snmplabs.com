#
# PySNMP MIB module BAS-PROV-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BAS-PROV-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:17:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
basProvInfo, = mibBuilder.importSymbols("BAS-MIB", "basProvInfo")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, MibIdentifier, iso, Counter32, ObjectIdentity, Unsigned32, Counter64, Bits, Integer32, ModuleIdentity, TimeTicks, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "MibIdentifier", "iso", "Counter32", "ObjectIdentity", "Unsigned32", "Counter64", "Bits", "Integer32", "ModuleIdentity", "TimeTicks", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
basProvInfoMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1))
if mibBuilder.loadTexts: basProvInfoMib.setLastUpdated('9901180900Z')
if mibBuilder.loadTexts: basProvInfoMib.setOrganization('Broadband Access Systems')
basProvObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1))
basProvServerId = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 1), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basProvServerId.setStatus('current')
basProvInfoLdapServerIpAddr = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 2), IpAddress()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basProvInfoLdapServerIpAddr.setStatus('current')
basProvInfoLdapServerPort = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basProvInfoLdapServerPort.setStatus('current')
basProvInfoLdapServerUserName = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basProvInfoLdapServerUserName.setStatus('current')
basProvInfoLdapServerPassword = MibScalar((1, 3, 6, 1, 4, 1, 3493, 2, 1, 4, 1, 1, 5), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: basProvInfoLdapServerPassword.setStatus('current')
mibBuilder.exportSymbols("BAS-PROV-MIB", basProvInfoLdapServerPassword=basProvInfoLdapServerPassword, basProvInfoLdapServerIpAddr=basProvInfoLdapServerIpAddr, basProvInfoLdapServerUserName=basProvInfoLdapServerUserName, basProvServerId=basProvServerId, basProvObjects=basProvObjects, basProvInfoLdapServerPort=basProvInfoLdapServerPort, basProvInfoMib=basProvInfoMib, PYSNMP_MODULE_ID=basProvInfoMib)
