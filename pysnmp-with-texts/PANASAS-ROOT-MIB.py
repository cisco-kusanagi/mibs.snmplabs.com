#
# PySNMP MIB module PANASAS-ROOT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PANASAS-ROOT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:36:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Unsigned32, IpAddress, Integer32, NotificationType, Counter32, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, ModuleIdentity, iso, Counter64, Gauge32, enterprises = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Unsigned32", "IpAddress", "Integer32", "NotificationType", "Counter32", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "ModuleIdentity", "iso", "Counter64", "Gauge32", "enterprises")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
panasas = ModuleIdentity((1, 3, 6, 1, 4, 1, 10159))
panasas.setRevisions(('2011-04-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: panasas.setRevisionsDescriptions(('1. Changed Panasas, Inc. company contact information.',))
if mibBuilder.loadTexts: panasas.setLastUpdated('201104070000Z')
if mibBuilder.loadTexts: panasas.setOrganization('Panasas, Inc')
if mibBuilder.loadTexts: panasas.setContactInfo('postal: Panasas, Inc 969 W. Maude Avenue Sunnyvale, CA 94085 phone: +1 408 215-6800 email: info@panasas.com')
if mibBuilder.loadTexts: panasas.setDescription('This is the root of the Panasas Enterprise MIB.')
panProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1))
panNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 1))
panHw = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 2))
panFs = MibIdentifier((1, 3, 6, 1, 4, 1, 10159, 1, 3))
mibBuilder.exportSymbols("PANASAS-ROOT-MIB", PYSNMP_MODULE_ID=panasas, panNotifications=panNotifications, panProducts=panProducts, panFs=panFs, panasas=panasas, panHw=panHw)
