#
# PySNMP MIB module WRS-MASTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/WRS-MASTER-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:23:44 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
iso, Unsigned32, IpAddress, ObjectIdentity, TimeTicks, MibIdentifier, Bits, ModuleIdentity, Counter32, NotificationType, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Gauge32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Unsigned32", "IpAddress", "ObjectIdentity", "TimeTicks", "MibIdentifier", "Bits", "ModuleIdentity", "Counter32", "NotificationType", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Gauge32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wrs = ModuleIdentity((1, 3, 6, 1, 4, 1, 731))
wrs.setRevisions(('2000-08-29 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: wrs.setRevisionsDescriptions(('Initial MIB creation.',))
if mibBuilder.loadTexts: wrs.setLastUpdated('200008290000Z')
if mibBuilder.loadTexts: wrs.setOrganization('Wind River Systems, Inc.')
if mibBuilder.loadTexts: wrs.setContactInfo('Wind River Systems, Inc. E-mail: support@windriver.com')
if mibBuilder.loadTexts: wrs.setDescription('WRS Master MIB OID defines and documentation.')
tms = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2))
idb = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 1))
tmsGeneric = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 2))
oemSwapi = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 3))
oemProd = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 4))
rmonMib = MibIdentifier((1, 3, 6, 1, 4, 1, 731, 2, 1, 1))
mibBuilder.exportSymbols("WRS-MASTER-MIB", tmsGeneric=tmsGeneric, PYSNMP_MODULE_ID=wrs, idb=idb, oemProd=oemProd, tms=tms, rmonMib=rmonMib, oemSwapi=oemSwapi, wrs=wrs)
