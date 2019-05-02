#
# PySNMP MIB module SONICWALL-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONICWALL-SMI
# Produced by pysmi-0.3.4 at Wed May  1 15:09:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, Counter32, MibIdentifier, Counter64, TimeTicks, ObjectIdentity, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, IpAddress, Gauge32, enterprises, Unsigned32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "Counter32", "MibIdentifier", "Counter64", "TimeTicks", "ObjectIdentity", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "IpAddress", "Gauge32", "enterprises", "Unsigned32", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sonicwall = ModuleIdentity((1, 3, 6, 1, 4, 1, 8741))
sonicwall.setRevisions(('2003-04-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: sonicwall.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: sonicwall.setLastUpdated('200304220000Z')
if mibBuilder.loadTexts: sonicwall.setOrganization('SonicWall, Inc.')
if mibBuilder.loadTexts: sonicwall.setContactInfo(' SonicWall Inc. Postal: 1143 Borregas Avenue Sunnyvale, CA 94089 USA Tel: +1 408 745 9600 Fax: +1 408 745 9300 E-mail: product@sonicwall.com')
if mibBuilder.loadTexts: sonicwall.setDescription('The MIB Module for Sonicwall enterprise.')
sonicwallFw = ObjectIdentity((1, 3, 6, 1, 4, 1, 8741, 1))
if mibBuilder.loadTexts: sonicwallFw.setStatus('current')
if mibBuilder.loadTexts: sonicwallFw.setDescription('sonicwallFw is the subtree for the sonicwall firewall production.')
mibBuilder.exportSymbols("SONICWALL-SMI", sonicwall=sonicwall, sonicwallFw=sonicwallFw, PYSNMP_MODULE_ID=sonicwall)
