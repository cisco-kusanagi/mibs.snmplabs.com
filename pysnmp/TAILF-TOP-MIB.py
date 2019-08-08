#
# PySNMP MIB module TAILF-TOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TAILF-TOP-MIB
# Produced by pysmi-0.3.4 at Wed Aug  7 20:00:11 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.7.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
enterprises, Gauge32, IpAddress, ModuleIdentity, Integer32, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Bits, MibIdentifier, ObjectIdentity, NotificationType, Unsigned32, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "enterprises", "Gauge32", "IpAddress", "ModuleIdentity", "Integer32", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Bits", "MibIdentifier", "ObjectIdentity", "NotificationType", "Unsigned32", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tailf = ModuleIdentity((1, 3, 6, 1, 4, 1, 24961))
tailf.setRevisions(('2011-03-01 00:00',))
if mibBuilder.loadTexts: tailf.setLastUpdated('201103010000Z')
if mibBuilder.loadTexts: tailf.setOrganization('Tail-f Systems AB')
tfProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 24961, 1))
if mibBuilder.loadTexts: tfProducts.setStatus('current')
tfModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 24961, 2))
if mibBuilder.loadTexts: tfModules.setStatus('current')
mibBuilder.exportSymbols("TAILF-TOP-MIB", tfProducts=tfProducts, tfModules=tfModules, PYSNMP_MODULE_ID=tailf, tailf=tailf)
