#
# PySNMP MIB module SIP-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SIP-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:56:28 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
reason, comment, percent, code, gwType, csID, port, timeOccurred, registrationStatus, csType, gwIP, gwID, moduleID = mibBuilder.importSymbols("AGGREGATED-EXT-MIB", "reason", "comment", "percent", "code", "gwType", "csID", "port", "timeOccurred", "registrationStatus", "csType", "gwIP", "gwID", "moduleID")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, Counter64, IpAddress, ObjectName, ModuleIdentity, Unsigned32, snmpModules, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, TimeTicks, Gauge32, ObjectIdentity, Bits, iso, Integer32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "Counter64", "IpAddress", "ObjectName", "ModuleIdentity", "Unsigned32", "snmpModules", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "TimeTicks", "Gauge32", "ObjectIdentity", "Bits", "iso", "Integer32", "NotificationType")
TextualConvention, TimeStamp, TestAndIncr, DisplayString, RowStatus, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "TimeStamp", "TestAndIncr", "DisplayString", "RowStatus", "TruthValue")
lucent = MibIdentifier((1, 3, 6, 1, 4, 1, 1751))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1))
softSwitch = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198))
sipDeviceServer = MibIdentifier((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5))
sipTraps = ModuleIdentity((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 0))
if mibBuilder.loadTexts: sipTraps.setLastUpdated('240701')
if mibBuilder.loadTexts: sipTraps.setOrganization('Lucent Technologies')
sipCSConnectionStatus = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 0, 0)).setObjects(("AGGREGATED-EXT-MIB", "timeOccurred"), ("AGGREGATED-EXT-MIB", "code"), ("AGGREGATED-EXT-MIB", "csID"), ("AGGREGATED-EXT-MIB", "csType"), ("AGGREGATED-EXT-MIB", "registrationStatus"), ("AGGREGATED-EXT-MIB", "reason"), ("AGGREGATED-EXT-MIB", "comment"))
if mibBuilder.loadTexts: sipCSConnectionStatus.setStatus('current')
sipDSError = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 0, 1)).setObjects(("AGGREGATED-EXT-MIB", "timeOccurred"), ("AGGREGATED-EXT-MIB", "code"), ("AGGREGATED-EXT-MIB", "reason"), ("AGGREGATED-EXT-MIB", "comment"))
if mibBuilder.loadTexts: sipDSError.setStatus('current')
sipCommandFailed = NotificationType((1, 3, 6, 1, 4, 1, 1751, 1, 1198, 5, 0, 2)).setObjects(("AGGREGATED-EXT-MIB", "timeOccurred"), ("AGGREGATED-EXT-MIB", "code"), ("AGGREGATED-EXT-MIB", "reason"), ("AGGREGATED-EXT-MIB", "comment"))
if mibBuilder.loadTexts: sipCommandFailed.setStatus('current')
mibBuilder.exportSymbols("SIP-TRAP-MIB", lucent=lucent, sipTraps=sipTraps, sipDeviceServer=sipDeviceServer, sipCommandFailed=sipCommandFailed, sipCSConnectionStatus=sipCSConnectionStatus, sipDSError=sipDSError, softSwitch=softSwitch, PYSNMP_MODULE_ID=sipTraps, products=products)
