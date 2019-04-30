#
# PySNMP MIB module QUANTUMBRIDGE-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/QUANTUMBRIDGE-REG
# Produced by pysmi-0.3.4 at Mon Apr 29 20:34:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, TimeTicks, NotificationType, Bits, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Integer32, Gauge32, Unsigned32, MibIdentifier, Counter32, IpAddress, enterprises, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "NotificationType", "Bits", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Integer32", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "IpAddress", "enterprises", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
quantumBridgeRegistrations = ModuleIdentity((1, 3, 6, 1, 4, 1, 4323, 1))
if mibBuilder.loadTexts: quantumBridgeRegistrations.setLastUpdated('9903202155Z')
if mibBuilder.loadTexts: quantumBridgeRegistrations.setOrganization('Quantum Bridge Communications Inc.')
quantumBridge = ObjectIdentity((1, 3, 6, 1, 4, 1, 4323))
if mibBuilder.loadTexts: quantumBridge.setStatus('current')
qbMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 4323, 2))
if mibBuilder.loadTexts: qbMibs.setStatus('current')
qbProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 4323, 3))
if mibBuilder.loadTexts: qbProducts.setStatus('current')
qb5000SystemID = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 3, 1))
qb3000SystemID = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 3, 2))
qb8000SystemID = MibIdentifier((1, 3, 6, 1, 4, 1, 4323, 3, 3))
mibBuilder.exportSymbols("QUANTUMBRIDGE-REG", quantumBridge=quantumBridge, qb8000SystemID=qb8000SystemID, PYSNMP_MODULE_ID=quantumBridgeRegistrations, qbMibs=qbMibs, qbProducts=qbProducts, quantumBridgeRegistrations=quantumBridgeRegistrations, qb5000SystemID=qb5000SystemID, qb3000SystemID=qb3000SystemID)
