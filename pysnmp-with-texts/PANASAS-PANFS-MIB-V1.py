#
# PySNMP MIB module PANASAS-PANFS-MIB-V1 (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANASAS-PANFS-MIB-V1
# Produced by pysmi-0.3.4 at Wed May  1 14:36:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
panProducts, = mibBuilder.importSymbols("PANASAS-ROOT-MIB", "panProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, IpAddress, Integer32, NotificationType, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, iso, Counter64, Gauge32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "IpAddress", "Integer32", "NotificationType", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "iso", "Counter64", "Gauge32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
panFs = ModuleIdentity((1, 3, 6, 1, 4, 1, 10159, 1, 3))
panFs.setRevisions(('2011-04-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: panFs.setRevisionsDescriptions(('1. Changed Panasas, Inc. company contact information.',))
if mibBuilder.loadTexts: panFs.setLastUpdated('201104070000Z')
if mibBuilder.loadTexts: panFs.setOrganization('Panasas, Inc')
if mibBuilder.loadTexts: panFs.setContactInfo('postal: Panasas, Inc 969 W. Maude Avenue Sunnyvale, CA 94085 phone: +1 408 215-6800 email: info@panasas.com')
if mibBuilder.loadTexts: panFs.setDescription('This defines the subcomponents of Panasas File System MIB.')
panEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 1))
panSystem = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 2))
panBSet = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 3))
panVol = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 4))
panPerf = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3, 5))
mibBuilder.exportSymbols("PANASAS-PANFS-MIB-V1", PYSNMP_MODULE_ID=panFs, panEvents=panEvents, panFs=panFs, panSystem=panSystem, panBSet=panBSet, panVol=panVol, panPerf=panPerf)
