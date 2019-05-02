#
# PySNMP MIB module LANCITY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LANCITY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:05:20 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, Counter32, NotificationType, ObjectIdentity, Unsigned32, enterprises, TimeTicks, Gauge32, iso, Counter64, Integer32, IpAddress, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Counter32", "NotificationType", "ObjectIdentity", "Unsigned32", "enterprises", "TimeTicks", "Gauge32", "iso", "Counter64", "Integer32", "IpAddress", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
lancity = ModuleIdentity((1, 3, 6, 1, 4, 1, 482))
if mibBuilder.loadTexts: lancity.setLastUpdated('9709061024Z')
if mibBuilder.loadTexts: lancity.setOrganization('Bay Networks Broadband Technologies Division')
if mibBuilder.loadTexts: lancity.setContactInfo('Dale Hokanson Postal: Bay Networks Broadband Technologies Division 200 Bulfinch Drive Andover, MA 01810 U.S.A. Phone: +1 508 682 1600 E-mail: support@lancity.com')
if mibBuilder.loadTexts: lancity.setDescription('This is a header for the Lancity enterprise MIB. All objects appear elsewhere.')
mibBuilder.exportSymbols("LANCITY-MIB", PYSNMP_MODULE_ID=lancity, lancity=lancity)
