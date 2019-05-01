#
# PySNMP MIB module LIGOWAVE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LIGOWAVE-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:07:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Counter32, ModuleIdentity, iso, Integer32, Counter64, Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, IpAddress, MibIdentifier, TimeTicks, ObjectIdentity, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "ModuleIdentity", "iso", "Integer32", "Counter64", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "IpAddress", "MibIdentifier", "TimeTicks", "ObjectIdentity", "enterprises")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ligowave = ModuleIdentity((1, 3, 6, 1, 4, 1, 32750))
ligowave.setRevisions(('2008-09-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ligowave.setRevisionsDescriptions(('First revision.',))
if mibBuilder.loadTexts: ligowave.setLastUpdated('200809050000Z')
if mibBuilder.loadTexts: ligowave.setOrganization('LigoWave')
if mibBuilder.loadTexts: ligowave.setContactInfo(' LigoWave Customer Support E-mail: support@ligowave.com')
if mibBuilder.loadTexts: ligowave.setDescription('LigoWave central configuration module.')
ligoProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 1))
ligoAdmin = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 2))
ligoMgmt = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 3))
ligoExperimental = MibIdentifier((1, 3, 6, 1, 4, 1, 32750, 7))
mibBuilder.exportSymbols("LIGOWAVE-MIB", ligoExperimental=ligoExperimental, PYSNMP_MODULE_ID=ligowave, ligowave=ligowave, ligoMgmt=ligoMgmt, ligoAdmin=ligoAdmin, ligoProducts=ligoProducts)
