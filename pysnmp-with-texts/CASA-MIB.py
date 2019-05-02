#
# PySNMP MIB module CASA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CASA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:47:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, MibIdentifier, TimeTicks, enterprises, ModuleIdentity, Integer32, iso, Counter64, Gauge32, Bits, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "MibIdentifier", "TimeTicks", "enterprises", "ModuleIdentity", "Integer32", "iso", "Counter64", "Gauge32", "Bits", "Unsigned32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
casa = ModuleIdentity((1, 3, 6, 1, 4, 1, 20858))
casa.setRevisions(('2006-03-22 00:00', '2006-03-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: casa.setRevisionsDescriptions(('Initial creation.', 'CASA mib root',))
if mibBuilder.loadTexts: casa.setLastUpdated('200407080000Z')
if mibBuilder.loadTexts: casa.setOrganization('Casa Systems Inc.')
if mibBuilder.loadTexts: casa.setContactInfo('10 New England Business Center Drive Andover, MA 01810 Tel: 978-688-6706 Fax: 978-688-6584 E-mail: pluo@casa-systems.com Peng Luo Casa Systems, Inc. ')
if mibBuilder.loadTexts: casa.setDescription('MIB module definition for Casa systems inc.')
mibBuilder.exportSymbols("CASA-MIB", PYSNMP_MODULE_ID=casa, casa=casa)
