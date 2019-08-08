#
# PySNMP MIB module TAILF-TOP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TAILF-TOP-MIB
# Produced by pysmi-0.3.4 at Thu Aug  8 14:21:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.7.0 by user davwang4
# Using Python version 2.7.15 (default, May  1 2018, 16:44:08) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, IpAddress, TimeTicks, Counter64, Unsigned32, enterprises, iso, Gauge32, ModuleIdentity, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "IpAddress", "TimeTicks", "Counter64", "Unsigned32", "enterprises", "iso", "Gauge32", "ModuleIdentity", "ObjectIdentity", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tailf = ModuleIdentity((1, 3, 6, 1, 4, 1, 24961))
tailf.setRevisions(('2011-03-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tailf.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tailf.setLastUpdated('201103010000Z')
if mibBuilder.loadTexts: tailf.setOrganization('Tail-f Systems AB')
if mibBuilder.loadTexts: tailf.setContactInfo('support@tail-f.com')
if mibBuilder.loadTexts: tailf.setDescription('The root MIB for Tail-f System AB')
tfProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 24961, 1))
if mibBuilder.loadTexts: tfProducts.setStatus('current')
if mibBuilder.loadTexts: tfProducts.setDescription('The root OBJECT IDENTIFIER from which sysObjectID values are assigned.')
tfModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 24961, 2))
if mibBuilder.loadTexts: tfModules.setStatus('current')
if mibBuilder.loadTexts: tfModules.setDescription('The root OBJECT IDENTIFIER to be used for MIB module registration.')
mibBuilder.exportSymbols("TAILF-TOP-MIB", tfProducts=tfProducts, tfModules=tfModules, tailf=tailf, PYSNMP_MODULE_ID=tailf)
