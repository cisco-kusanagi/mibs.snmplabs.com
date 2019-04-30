#
# PySNMP MIB module PANASAS-PANFS-MIB-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANASAS-PANFS-MIB-V1
# Produced by pysmi-0.3.4 at Mon Apr 29 20:27:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
panProducts, = mibBuilder.importSymbols("PANASAS-ROOT-MIB", "panProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ObjectIdentity, Integer32, Unsigned32, MibIdentifier, NotificationType, ModuleIdentity, TimeTicks, Counter64, Gauge32, Counter32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ObjectIdentity", "Integer32", "Unsigned32", "MibIdentifier", "NotificationType", "ModuleIdentity", "TimeTicks", "Counter64", "Gauge32", "Counter32", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
panFs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10159, 1, 3))
panFs.setRevisions(('2011-04-07 00:00',))
if mibBuilder.loadTexts: panFs.setLastUpdated('201104070000Z')
if mibBuilder.loadTexts: panFs.setOrganization('Panasas, Inc')
panEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1))
panSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2))
panBSet = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 3))
panVol = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 4))
panPerf = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 5))
mibBuilder.exportSymbols("PANASAS-PANFS-MIB-V1", PYSNMP_MODULE_ID=panFs, panFs=panFs, panPerf=panPerf, panSystem=panSystem, panVol=panVol, panEvents=panEvents, panBSet=panBSet)
