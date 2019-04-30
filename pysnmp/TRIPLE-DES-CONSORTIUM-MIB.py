#
# PySNMP MIB module TRIPLE-DES-CONSORTIUM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRIPLE-DES-CONSORTIUM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:20:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
snmpModules, Unsigned32, Bits, ObjectIdentity, Integer32, Counter32, Gauge32, TimeTicks, NotificationType, MibIdentifier, IpAddress, iso, enterprises, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "snmpModules", "Unsigned32", "Bits", "ObjectIdentity", "Integer32", "Counter32", "Gauge32", "TimeTicks", "NotificationType", "MibIdentifier", "IpAddress", "iso", "enterprises", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention, AutonomousType = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "AutonomousType")
tripleDESConsortiumMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 14832))
tripleDESConsortiumMIB.setRevisions(('2003-02-03 00:00',))
if mibBuilder.loadTexts: tripleDESConsortiumMIB.setLastUpdated('200302030000Z')
if mibBuilder.loadTexts: tripleDESConsortiumMIB.setOrganization('Triple DES Consortium')
tripleDESConsortiumPrivProtocols = MibIdentifier((1, 3, 6, 1, 4, 1, 14832, 1))
usm3DESPrivProtocol = ObjectIdentity((1, 3, 6, 1, 4, 1, 14832, 1, 1))
if mibBuilder.loadTexts: usm3DESPrivProtocol.setStatus('current')
mibBuilder.exportSymbols("TRIPLE-DES-CONSORTIUM-MIB", PYSNMP_MODULE_ID=tripleDESConsortiumMIB, tripleDESConsortiumMIB=tripleDESConsortiumMIB, tripleDESConsortiumPrivProtocols=tripleDESConsortiumPrivProtocols, usm3DESPrivProtocol=usm3DESPrivProtocol)
