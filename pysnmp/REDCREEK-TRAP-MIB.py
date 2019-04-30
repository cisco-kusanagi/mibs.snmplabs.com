#
# PySNMP MIB module REDCREEK-TRAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/REDCREEK-TRAP-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:46:47 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
rcTrap, = mibBuilder.importSymbols("RCV3", "rcTrap")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, TimeTicks, Bits, NotificationType, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter32, iso, ObjectIdentity, NotificationType, ModuleIdentity, Counter64, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "TimeTicks", "Bits", "NotificationType", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter32", "iso", "ObjectIdentity", "NotificationType", "ModuleIdentity", "Counter64", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
rcBadSignature = NotificationType((1, 3, 6, 1, 4, 1, 1958, 1, 1, 5) + (0,1))
rcHashFailed = NotificationType((1, 3, 6, 1, 4, 1, 1958, 1, 1, 5) + (0,2))
rcFirmwareDownloadSucceded = NotificationType((1, 3, 6, 1, 4, 1, 1958, 1, 1, 5) + (0,3))
rcFirmwareDownloadFailed = NotificationType((1, 3, 6, 1, 4, 1, 1958, 1, 1, 5) + (0,4))
rcTunnelStatusThreshold = NotificationType((1, 3, 6, 1, 4, 1, 1958, 1, 1, 5) + (0,5))
mibBuilder.exportSymbols("REDCREEK-TRAP-MIB", rcBadSignature=rcBadSignature, rcTunnelStatusThreshold=rcTunnelStatusThreshold, rcFirmwareDownloadFailed=rcFirmwareDownloadFailed, rcFirmwareDownloadSucceded=rcFirmwareDownloadSucceded, rcHashFailed=rcHashFailed)
