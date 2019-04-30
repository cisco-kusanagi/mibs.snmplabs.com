#
# PySNMP MIB module IBMAPPNMEMORY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IBMAPPNMEMORY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:39:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, ObjectIdentity, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter32, Counter64, Gauge32, enterprises, Integer32, NotificationType, ModuleIdentity, Bits, TimeTicks, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ObjectIdentity", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter32", "Counter64", "Gauge32", "enterprises", "Integer32", "NotificationType", "ModuleIdentity", "Bits", "TimeTicks", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ibm = MibIdentifier((1, 3, 6, 1, 4, 1, 2))
ibmProd = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6))
ibm6611 = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 2))
ibmappn = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 2, 13))
ibmappnNode = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1))
ibmappnMemoryUse = MibIdentifier((1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7))
ibmappnMemorySize = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmappnMemorySize.setStatus('mandatory')
ibmappnMemoryUsed = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmappnMemoryUsed.setStatus('mandatory')
ibmappnMemoryWarnThresh = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 3), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmappnMemoryWarnThresh.setStatus('mandatory')
ibmappnMemoryCritThresh = MibScalar((1, 3, 6, 1, 4, 1, 2, 6, 2, 13, 1, 7, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 2147483647))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ibmappnMemoryCritThresh.setStatus('mandatory')
mibBuilder.exportSymbols("IBMAPPNMEMORY-MIB", ibmappnMemorySize=ibmappnMemorySize, ibmappn=ibmappn, ibmappnMemoryWarnThresh=ibmappnMemoryWarnThresh, ibmProd=ibmProd, ibmappnMemoryUse=ibmappnMemoryUse, ibmappnMemoryUsed=ibmappnMemoryUsed, ibmappnMemoryCritThresh=ibmappnMemoryCritThresh, ibm=ibm, ibmappnNode=ibmappnNode, ibm6611=ibm6611)
