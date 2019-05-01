#
# PySNMP MIB module STN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/STN-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:11:35 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, IpAddress, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Gauge32, Counter64, ObjectIdentity, Unsigned32, Integer32, Bits, Counter32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "IpAddress", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Gauge32", "Counter64", "ObjectIdentity", "Unsigned32", "Integer32", "Bits", "Counter32", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
stnProducts, stnMibModules = mibBuilder.importSymbols("SPRING-TIDE-NETWORKS-SMI", "stnProducts", "stnMibModules")
stnProductsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 3551, 5, 2))
stnProductsMIB.setRevisions(('1999-05-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: stnProductsMIB.setRevisionsDescriptions(('This MIB module defines MIB objects which provide mechanisms to remotely monitor the parameters used by an SNMP entity for the generation of SNMP messages.',))
if mibBuilder.loadTexts: stnProductsMIB.setLastUpdated('0002160000Z')
if mibBuilder.loadTexts: stnProductsMIB.setOrganization('Spring Tide Networks, Inc.')
if mibBuilder.loadTexts: stnProductsMIB.setContactInfo(' Spring Tide Networks, Inc. Customer Service Postal: 3 Clock Tower Place Maynard, MA 01754 Tel: 1 888-786-4357 Email: stncs@springtidenet.com ')
if mibBuilder.loadTexts: stnProductsMIB.setDescription('The initial revision.')
stn5000 = MibIdentifier((1, 3, 6, 1, 4, 1, 3551, 1, 1))
mibBuilder.exportSymbols("STN-PRODUCTS-MIB", stn5000=stn5000, stnProductsMIB=stnProductsMIB, PYSNMP_MODULE_ID=stnProductsMIB)
