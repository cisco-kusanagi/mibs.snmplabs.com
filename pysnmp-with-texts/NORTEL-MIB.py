#
# PySNMP MIB module NORTEL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NORTEL-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:42:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Unsigned32, Bits, TimeTicks, Gauge32, IpAddress, MibIdentifier, Counter64, ModuleIdentity, Counter32, enterprises, NotificationType, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Unsigned32", "Bits", "TimeTicks", "Gauge32", "IpAddress", "MibIdentifier", "Counter64", "ModuleIdentity", "Counter32", "enterprises", "NotificationType", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
nortel = ModuleIdentity((1, 3, 6, 1, 4, 1, 562))
if mibBuilder.loadTexts: nortel.setLastUpdated('200305010000Z')
if mibBuilder.loadTexts: nortel.setOrganization('Northern Telecom Ltd.')
if mibBuilder.loadTexts: nortel.setContactInfo(' Nortel Networks 8200 Dixie Road Brampton, Ontario L6T 5P6 Canada 1-800-4Nortel www.nortelnetworks.com')
if mibBuilder.loadTexts: nortel.setDescription('The Nortel Networks top-level MIB definition.')
mibBuilder.exportSymbols("NORTEL-MIB", PYSNMP_MODULE_ID=nortel, nortel=nortel)
