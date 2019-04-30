#
# PySNMP MIB module CIENA-GLOBAL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CIENA-GLOBAL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:31:40 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
cienaCommon, = mibBuilder.importSymbols("CIENA-SMI", "cienaCommon")
CienaGlobalSeverity, = mibBuilder.importSymbols("CIENA-TC", "CienaGlobalSeverity")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, NotificationType, Gauge32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, Counter32, ObjectIdentity, MibIdentifier, ModuleIdentity, Bits, TimeTicks, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "NotificationType", "Gauge32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "Counter32", "ObjectIdentity", "MibIdentifier", "ModuleIdentity", "Bits", "TimeTicks", "Integer32")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
cienaGlobal = ModuleIdentity((1, 3, 6, 1, 4, 1, 1271, 1, 3))
if mibBuilder.loadTexts: cienaGlobal.setLastUpdated('201003280000Z')
if mibBuilder.loadTexts: cienaGlobal.setOrganization('Ciena, Inc.')
cienaGlobalSeverity = MibScalar((1, 3, 6, 1, 4, 1, 1271, 1, 3, 1), CienaGlobalSeverity()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaGlobalSeverity.setStatus('current')
cienaGlobalMacAddress = MibScalar((1, 3, 6, 1, 4, 1, 1271, 1, 3, 2), MacAddress()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: cienaGlobalMacAddress.setStatus('current')
mibBuilder.exportSymbols("CIENA-GLOBAL-MIB", cienaGlobal=cienaGlobal, cienaGlobalSeverity=cienaGlobalSeverity, PYSNMP_MODULE_ID=cienaGlobal, cienaGlobalMacAddress=cienaGlobalMacAddress)
