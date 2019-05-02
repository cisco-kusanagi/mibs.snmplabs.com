#
# PySNMP MIB module CASA-ID-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CASA-ID-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
casa, = mibBuilder.importSymbols("CASA-MIB", "casa")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, iso, Counter32, NotificationType, MibIdentifier, IpAddress, ModuleIdentity, TimeTicks, Unsigned32, Gauge32, Counter64, ObjectIdentity, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "iso", "Counter32", "NotificationType", "MibIdentifier", "IpAddress", "ModuleIdentity", "TimeTicks", "Unsigned32", "Gauge32", "Counter64", "ObjectIdentity", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
casaIdMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 20858, 2))
casaIdMib.setRevisions(('1900-04-07 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: casaIdMib.setRevisionsDescriptions(('Initial Version',))
if mibBuilder.loadTexts: casaIdMib.setLastUpdated('200608150000Z')
if mibBuilder.loadTexts: casaIdMib.setOrganization('CASA SYSTEMS INC')
if mibBuilder.loadTexts: casaIdMib.setContactInfo('PENG LUO CASA SYSTEMS INC. 10 NEW ENGLAND BUSINESS CENTER DRIVE, SUITE 110 ANDOVER, MA U.S.A. Phone: +1 978 409 6281 - EXT 15 E-mail: pluo@casa-systems.com')
if mibBuilder.loadTexts: casaIdMib.setDescription("CASA SYSTEMS' enterprise MIB Module")
casa2100System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 1))
casa2200System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 20))
casa2300System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 30))
casa2800System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 40))
casa3000System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 50))
casa6000System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 100))
casa10000System = MibIdentifier((1, 3, 6, 1, 4, 1, 20858, 2, 200))
mibBuilder.exportSymbols("CASA-ID-MIB", casa2200System=casa2200System, casa6000System=casa6000System, casa2100System=casa2100System, casa3000System=casa3000System, PYSNMP_MODULE_ID=casaIdMib, casaIdMib=casaIdMib, casa10000System=casa10000System, casa2300System=casa2300System, casa2800System=casa2800System)
