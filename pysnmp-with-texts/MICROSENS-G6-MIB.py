#
# PySNMP MIB module MICROSENS-G6-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MICROSENS-G6-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:17:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, ModuleIdentity, MibIdentifier, enterprises, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Unsigned32, Bits, Integer32, Counter64, Counter32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "ModuleIdentity", "MibIdentifier", "enterprises", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Unsigned32", "Bits", "Integer32", "Counter64", "Counter32", "Gauge32")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
microsens = ModuleIdentity((1, 3, 6, 1, 4, 1, 3181))
microsens.setRevisions(('2015-05-22 10:58',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: microsens.setRevisionsDescriptions(('File creation',))
if mibBuilder.loadTexts: microsens.setLastUpdated('201505221058Z')
if mibBuilder.loadTexts: microsens.setOrganization('MICROSENS GmbH & Co. KG')
if mibBuilder.loadTexts: microsens.setContactInfo('Kueferstrasse 16 D-59067 Hamm Germany support@microsens.de http://www.microsens.de')
if mibBuilder.loadTexts: microsens.setDescription('Microsens private MIB for Generation 6 Ethernet Switches')
managedSwitches = MibIdentifier((1, 3, 6, 1, 4, 1, 3181, 10))
g6 = MibIdentifier((1, 3, 6, 1, 4, 1, 3181, 10, 6))
mibBuilder.exportSymbols("MICROSENS-G6-MIB", microsens=microsens, managedSwitches=managedSwitches, g6=g6, PYSNMP_MODULE_ID=microsens)
