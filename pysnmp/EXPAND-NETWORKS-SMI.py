#
# PySNMP MIB module EXPAND-NETWORKS-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EXPAND-NETWORKS-SMI
# Produced by pysmi-0.3.4 at Mon Apr 29 18:52:49 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, ModuleIdentity, Integer32, Bits, TimeTicks, Unsigned32, MibIdentifier, Counter64, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Gauge32, iso, NotificationType, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Integer32", "Bits", "TimeTicks", "Unsigned32", "MibIdentifier", "Counter64", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Gauge32", "iso", "NotificationType", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
expand_networks = MibIdentifier((1, 3, 6, 1, 4, 1, 3405)).setLabel("expand-networks")
expandSystemId = MibScalar((1, 3, 6, 1, 4, 1, 3405, 1), ObjectIdentifier()).setMaxAccess("readonly")
if mibBuilder.loadTexts: expandSystemId.setStatus('mandatory')
expandProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 2))
acceleratorOs = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 3))
p2pAccelerator = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 4))
management = MibIdentifier((1, 3, 6, 1, 4, 1, 3405, 10))
mibBuilder.exportSymbols("EXPAND-NETWORKS-SMI", acceleratorOs=acceleratorOs, expand_networks=expand_networks, expandSystemId=expandSystemId, expandProducts=expandProducts, p2pAccelerator=p2pAccelerator, management=management)
