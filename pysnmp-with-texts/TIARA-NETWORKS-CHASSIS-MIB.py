#
# PySNMP MIB module TIARA-NETWORKS-CHASSIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TIARA-NETWORKS-CHASSIS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:16:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Gauge32, TimeTicks, NotificationType, Unsigned32, Counter32, IpAddress, ModuleIdentity, Bits, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, MibIdentifier, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "TimeTicks", "NotificationType", "Unsigned32", "Counter32", "IpAddress", "ModuleIdentity", "Bits", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "MibIdentifier", "Counter64", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tiaraMgmt, = mibBuilder.importSymbols("TIARA-NETWORKS-SMI", "tiaraMgmt")
tiaraChassisMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 3174, 2, 2))
tiaraChassisMib.setRevisions(('1900-01-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: tiaraChassisMib.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: tiaraChassisMib.setLastUpdated('0001270000Z')
if mibBuilder.loadTexts: tiaraChassisMib.setOrganization('Tiara Networks, Inc.')
if mibBuilder.loadTexts: tiaraChassisMib.setContactInfo(' Tiara Networks Customer Support 525 Race Street, Suite 100, San Jose, CA 95126 USA Tel: +1 408-216-4700 Fax: +1 408-216-4701 E-mail: support@tiaranetworks.com')
if mibBuilder.loadTexts: tiaraChassisMib.setDescription('Listing and brief description of Tiara Networks product model numbers.')
chassisType = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 2, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisType.setStatus('current')
if mibBuilder.loadTexts: chassisType.setDescription('The chassis type.')
chassisSerialNumber = MibScalar((1, 3, 6, 1, 4, 1, 3174, 2, 2, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 30))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisSerialNumber.setStatus('current')
if mibBuilder.loadTexts: chassisSerialNumber.setDescription('The serial number of the chassis.')
mibBuilder.exportSymbols("TIARA-NETWORKS-CHASSIS-MIB", chassisSerialNumber=chassisSerialNumber, tiaraChassisMib=tiaraChassisMib, chassisType=chassisType, PYSNMP_MODULE_ID=tiaraChassisMib)
