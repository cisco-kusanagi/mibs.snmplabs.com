#
# PySNMP MIB module LEGATO-CLUSTER-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/LEGATO-CLUSTER-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:55:58 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, TimeTicks, enterprises, Bits, NotificationType, ObjectIdentity, Integer32, NotificationType, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Counter32, Counter64, iso, Unsigned32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "enterprises", "Bits", "NotificationType", "ObjectIdentity", "Integer32", "NotificationType", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Counter32", "Counter64", "iso", "Unsigned32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

legatoSoftware = MibIdentifier((1, 3, 6, 1, 4, 1, 1676))
products = MibIdentifier((1, 3, 6, 1, 4, 1, 1676, 1))
legatoCluster = MibIdentifier((1, 3, 6, 1, 4, 1, 1676, 1, 4))
clusterMessage = MibIdentifier((1, 3, 6, 1, 4, 1, 1676, 1, 4, 1))
trapSeverity = MibScalar((1, 3, 6, 1, 4, 1, 1676, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("info", 1), ("warning", 2), ("severe", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapSeverity.setStatus('mandatory')
trapText = MibScalar((1, 3, 6, 1, 4, 1, 1676, 1, 4, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: trapText.setStatus('mandatory')
legatoClusterUserTrap = NotificationType((1, 3, 6, 1, 4, 1, 1676, 1, 4) + (0,1)).setObjects(("LEGATO-CLUSTER-MIB", "trapText"), ("LEGATO-CLUSTER-MIB", "trapSeverity"))
mibBuilder.exportSymbols("LEGATO-CLUSTER-MIB", legatoSoftware=legatoSoftware, clusterMessage=clusterMessage, trapText=trapText, legatoCluster=legatoCluster, trapSeverity=trapSeverity, legatoClusterUserTrap=legatoClusterUserTrap, DisplayString=DisplayString, products=products)
