#
# PySNMP MIB module ROUTER-OIDS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ROUTER-OIDS
# Produced by pysmi-0.3.4 at Wed May  1 11:44:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
ctronExp, ctNetwork = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctronExp", "ctNetwork")
networkType, = mibBuilder.importSymbols("CTRON-OIDS", "networkType")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, TimeTicks, Counter32, Integer32, Counter64, NotificationType, ObjectIdentity, iso, MibIdentifier, ModuleIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "TimeTicks", "Counter32", "Integer32", "Counter64", "NotificationType", "ObjectIdentity", "iso", "MibIdentifier", "ModuleIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ntProtoSuites = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1))
ntIpRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1))
ntIpxRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2))
ntDecIVRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3))
ntAtRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4))
ntAppnRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5))
ntIpRip = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 1))
ntIpOspf = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 2))
ntIpFib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 3))
ntIpArp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 4))
ntIpAc1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 5))
ntIpFwdEng = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 6))
ntIpPortRedirect = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 7))
ntIpEventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 8))
ntIpAddressTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 1, 9))
ntIpxRip = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 1))
ntIpxSap = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 2))
ntIpxFib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 3))
ntIpxAc1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 5))
ntIpxFwdEng = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 6))
ntIpxPortRedirect = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 7))
ntIpxEventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 8))
ntIpxAddressTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 9))
ntIpxEcho = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 10))
ntIpxBroadcast = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 11))
ntIpxNetbios = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 2, 12))
ntDecIVLevel1 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 1))
ntDecIVLevel2 = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 2))
ntDecIVFib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 3))
ntDecIVAcl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 5))
ntDecIVFwdEng = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 6))
ntDecIVPportRedirect = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 7))
ntDecIVEventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 8))
ntDecIVAddressTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 3, 9))
ntAtRtgProt = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 1))
ntAtFib = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 3))
ntAtArp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 4))
ntAtAcl = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 5))
ntAtFwdEng = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 6))
ntAtEventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 8))
ntAtAddressTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 4, 9))
ntAppnFwdEng = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5, 6))
ntAppnEventLog = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5, 8))
ntAppnExtensionTable = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5, 9))
ntAppnIsr = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 3, 7, 1, 5, 10))
ctRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2))
ctHighLevelView = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 2))
ctProtoSuites = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3))
ctApplicationView = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 2, 1))
ctIpRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 1))
ctIpxRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 2))
ctDecIVRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 3))
ctAtRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 4))
ctAppnRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 3, 2, 3, 5))
ctronRouterExp = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2))
nwRouter = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2))
nwRtrMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 1))
nwRtrHighLevelView = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 2))
nwRtrProtoSuites = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 2, 2, 2, 3))
mibBuilder.exportSymbols("ROUTER-OIDS", ntProtoSuites=ntProtoSuites, ntDecIVAcl=ntDecIVAcl, ctAtRouter=ctAtRouter, ntDecIVLevel2=ntDecIVLevel2, ctProtoSuites=ctProtoSuites, ntIpFib=ntIpFib, ctDecIVRouter=ctDecIVRouter, ntAtEventLog=ntAtEventLog, ntDecIVEventLog=ntDecIVEventLog, ntAtRtgProt=ntAtRtgProt, ntAppnFwdEng=ntAppnFwdEng, ntAtFib=ntAtFib, ntIpAddressTable=ntIpAddressTable, ntIpxSap=ntIpxSap, ntIpRip=ntIpRip, ntIpAc1=ntIpAc1, ntAppnIsr=ntAppnIsr, ctIpxRouter=ctIpxRouter, ntIpxRip=ntIpxRip, nwRtrMibs=nwRtrMibs, ntAppnExtensionTable=ntAppnExtensionTable, ntIpEventLog=ntIpEventLog, ntDecIVRouter=ntDecIVRouter, ntIpxFwdEng=ntIpxFwdEng, ntIpxBroadcast=ntIpxBroadcast, ctAppnRouter=ctAppnRouter, ntIpxFib=ntIpxFib, ctIpRouter=ctIpRouter, ntIpRouter=ntIpRouter, nwRtrProtoSuites=nwRtrProtoSuites, nwRouter=nwRouter, ntAtFwdEng=ntAtFwdEng, ntIpxAc1=ntIpxAc1, ntDecIVAddressTable=ntDecIVAddressTable, ntIpPortRedirect=ntIpPortRedirect, ntAtArp=ntAtArp, ntIpxRouter=ntIpxRouter, ntIpxAddressTable=ntIpxAddressTable, ntDecIVFib=ntDecIVFib, ntIpxEventLog=ntIpxEventLog, ntIpxEcho=ntIpxEcho, ntAtAddressTable=ntAtAddressTable, ntDecIVPportRedirect=ntDecIVPportRedirect, ntIpOspf=ntIpOspf, ctApplicationView=ctApplicationView, ctronRouterExp=ctronRouterExp, ntIpFwdEng=ntIpFwdEng, ntDecIVFwdEng=ntDecIVFwdEng, ntIpxPortRedirect=ntIpxPortRedirect, ntAtAcl=ntAtAcl, ctHighLevelView=ctHighLevelView, ntAppnEventLog=ntAppnEventLog, ctRouter=ctRouter, ntDecIVLevel1=ntDecIVLevel1, ntIpxNetbios=ntIpxNetbios, ntAppnRouter=ntAppnRouter, ntAtRouter=ntAtRouter, ntIpArp=ntIpArp, nwRtrHighLevelView=nwRtrHighLevelView)
