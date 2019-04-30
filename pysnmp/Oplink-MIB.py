#
# PySNMP MIB module Oplink-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Oplink-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:26:48 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, Integer32, NotificationType, Unsigned32, ModuleIdentity, enterprises, IpAddress, Counter64, MibIdentifier, TimeTicks, Gauge32, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "Integer32", "NotificationType", "Unsigned32", "ModuleIdentity", "enterprises", "IpAddress", "Counter64", "MibIdentifier", "TimeTicks", "Gauge32", "ObjectIdentity", "Bits")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oplink = ModuleIdentity((1, 3, 6, 1, 4, 1, 19547))
oplink.setRevisions(('2013-04-02 15:00',))
if mibBuilder.loadTexts: oplink.setLastUpdated('201304021500Z')
if mibBuilder.loadTexts: oplink.setOrganization('OPLINK')
mngdproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 19547, 1))
mibBuilder.exportSymbols("Oplink-MIB", mngdproducts=mngdproducts, oplink=oplink, PYSNMP_MODULE_ID=oplink)
